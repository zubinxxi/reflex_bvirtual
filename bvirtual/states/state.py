import pathlib
import reflex as rx
import reflex_local_auth
from os import remove
from typing import Any, Optional

from sqlmodel import select
from bvirtual.models.auth.auth_models import UserInfo
from bvirtual.models.categorys.categorys_models import Categorys
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

    