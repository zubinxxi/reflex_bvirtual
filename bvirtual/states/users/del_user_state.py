from typing import Any
import reflex as rx
from sqlmodel import select

# Modelos
from reflex_local_auth.user import LocalUser
from bvirtual.models.auth.auth_models import UserInfo

# Estado
from bvirtual.states.users.users_state import UserInfoState

class DeleteUserState(rx.State):
    """State para eliminar usuarios."""

    @rx.event
    def delete_user(self, user: UserInfo):
        try:

            with rx.session() as session:
                user_to_delete = session.exec(
                    select(LocalUser).where(LocalUser.id == user.user_id)).first()
                session.delete(user_to_delete)
                session.commit()

                yield UserInfoState.list_users()
                yield rx.toast.success(f"Usuario \"{user.name}\" eliminado con ¡ÉXITO!", duration=5000, position="top-right")  
        except Exception as e:
            yield rx.toast.error(f"Error al eliminar el usuario: {str(e)}", duration=5000, position="top-center")  
            print(f"Error al eliminar el usuario: {str(e)}")