import pathlib
import reflex as rx
import reflex_local_auth
from os import remove
from typing import Any, Optional
from sqlmodel import desc, select, or_, func
from sqlalchemy.orm import joinedload # Importar joinedload

# Modelos
from bvirtual.models.auth.auth_models import UserInfo
from bvirtual.models.categorys.categorys_models import Categorys
from bvirtual.models.documents.document_models import Documents
from bvirtual.models.shelves.shelves_models import Shelves

# Clase estado personalizada para manejar la autenticación y obtener información del usuario
class MyLocalAuthState(reflex_local_auth.LocalAuthState):
    @rx.var(cache=True)
    def authenticated_user_info(self) -> Optional[UserInfo]:
        if self.authenticated_user.id < 0:
            return
        with rx.session() as session:
            return session.exec(
                UserInfo.select().where(UserInfo.user_id == self.authenticated_user.id)
            ).one_or_none() 
        

class MenuItemsStates(rx.State):
    categorys: list[Categorys] = []
    shelves: list[Shelves] = []
    today: str= ''

    # Listar Categorías y estantes
    @rx.event
    def items_menu(self):
        """Get users from the database."""
        with rx.session() as session:
            # Primero, Construir la consulta base, uniendo las tablas
            self.categorys = session.exec(select(Categorys)).all()
            self.shelves= session.exec(select(Shelves)).all()

class IndexState(rx.State):
    documents: list[Documents] = []
    search: str
    category_name: str # Nombre de la categoría seleccionada
    shelve_name: str # Nombre del estante seleccionado

    all_category_names: list[str] = [] # Lista de nombres de categorías que serán enviadas al frontend
    all_shelve_names: list[str] = [] # Lista de nombres de estentes que serán enviados al frontend

    #Paginado
    total_items: int
    offset: int = 0
    limit: int = 8  # Número de documentos por página
        
    
    # Función para manejar la búsqueda
    @rx.event
    def set_search(self, search):
        """Set the search query."""
        self.search = search
        return self.list_documents()
    
    # Funciones computadas para el paginado
    @rx.var(cache=True)
    def page_number(self) -> int:
        return (
            (self.offset // self.limit)
            + 1
            + (1 if self.offset % self.limit else 0)
        )

    @rx.var(cache=True)
    def total_pages(self) -> int:
        return self.total_items // self.limit + (
            1 if self.total_items % self.limit else 0
        )

    #Funciones utilizadas para la paginación
    @rx.event
    def prev_page(self):
        self.offset = max(self.offset - self.limit, 0)
        self.list_documents()

    @rx.event
    def next_page(self):
        if self.offset + self.limit < self.total_items:
            self.offset += self.limit
        self.list_documents()


    def _get_total_items(self):
        """Return the total number of items in the UserInfo table."""
        with rx.session() as session:
            self.total_items = session.exec(
                select(func.count(Documents.id))
            ).one()

    def set_limit(self, limit: str):
        """Set the number of items per page."""
        self.limit = int(limit)
        self.offset = 0  # Reset to the first page
        self.list_documents()

    # Metodo para traer las categorías
    def load_categorys(self):
        with rx.session() as session:
            self.all_category_names = session.exec(select(Categorys.description)).all()

    # Metodo para traer los estantes        
    def load_shelves(self):
        self.load_categorys()
        with rx.session() as session:
            self.all_shelve_names = session.exec(select(Shelves.description)).all()


    # Eventos que traen el nombre de la categoría y el estante desde los combos (select), y los asignan a las variables de estado
    @rx.event
    def set_category_name(self, category:str):
        self.category_name = category
        

    @rx.event
    def set_shelve_name(self, shelve: str):
        self.shelve_name = shelve

    # Listar Documentos
    @rx.event
    def list_documents(self):
        """Get documents from the database."""
        with rx.session() as session:
            # Primero, Construir la consulta base, uniendo las tablas
            query = select(Documents).join(Categorys).join(Shelves).order_by(desc(Documents.id))
            # Construir la consulta base con joinedload
            query = query.options(
                joinedload(Documents.categorys),
                joinedload(Documents.shelves),
            )
            
            # Aplicar la lógica de búsqueda si existe un término
            if self.search or self.category_name or self.shelve_name:
                query = query.where(
                    or_(
                        Documents.name.contains(self.search),
                        Categorys.description.contains(self.category_name),
                        Shelves.description.contains(self.shelve_name),
                    ),
                )
                self.documents = session.exec(query).all()[::-1]
            else:
                # Si no hay búsqueda, aplicar paginación
                self._get_total_items() # Se debe llamar aquí para tener el total antes de la paginación
                query = query.offset(self.offset).limit(self.limit)
                self.documents = session.exec(query).all()
    