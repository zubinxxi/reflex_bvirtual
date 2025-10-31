
import reflex as rx
import reflex_local_auth
from sqlmodel import select, or_, func
from sqlalchemy.orm import joinedload # Importar joinedload

# Modelos
from reflex_local_auth.user import LocalUser
from bvirtual.models.auth.auth_models import UserInfo, User_Role


# Clase estado para la pagina de usuarios 
class UserInfoState(reflex_local_auth.RegistrationState):
    users: list[UserInfo] = []
    search: str

    #Paginado
    total_items: int
    offset: int = 0
    limit: int = 10  # Número de usuarios por página

    # Función para obtener el valor de switch is_admin
    @rx.event
    def set_is_admin(self, admin: bool):
        self.sw_is_admin = admin
    
    # Función para manejar la búsqueda
    @rx.event
    def set_search(self, search):
        """Set the search query."""
        self.search = search
        return self.list_users()
    
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
        self.list_users()

    @rx.event
    def next_page(self):
        if self.offset + self.limit < self.total_items:
            self.offset += self.limit
        self.list_users()


    def _get_total_items(self):
        """Return the total number of items in the UserInfo table."""
        with rx.session() as session:
            self.total_items = session.exec(
                select(func.count(UserInfo.id))
            ).one()

    def set_limit(self, limit: str):
        """Set the number of items per page."""
        self.limit = int(limit)
        self.offset = 0  # Reset to the first page
        self.list_users()

    # Listar Usuarios
    @rx.event
    def list_users(self):
        """Get users from the database."""
        with rx.session() as session:
            # Primero, Construir la consulta base, uniendo las tablas
            query = select(UserInfo).join(LocalUser).join(User_Role)
            # Construir la consulta base con joinedload
            query = query.options(
                joinedload(UserInfo.localuser),
                joinedload(UserInfo.user_role),
            )
            
            # Aplicar la lógica de búsqueda si existe un término
            if self.search:
                query = query.where(
                    or_(
                        UserInfo.name.contains(self.search),
                        UserInfo.email.contains(self.search),
                        LocalUser.username.contains(self.search),
                        User_Role.name.contains(self.search),
                    ),
                )
                self.users = session.exec(query).all()[::-1]
            else:
                # Si no hay búsqueda, aplicar paginación
                self._get_total_items() # Se debe llamar aquí para tener el total antes de la paginación
                query = query.offset(self.offset).limit(self.limit)
                self.users = session.exec(query).all()  