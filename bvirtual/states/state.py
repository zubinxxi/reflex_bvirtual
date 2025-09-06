import reflex as rx
import reflex_local_auth
from typing import Optional
from bvirtual.models.auth.auth_models import UserInfo

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