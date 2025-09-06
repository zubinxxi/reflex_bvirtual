import reflex as rx
from typing import Any, Optional
from sqlmodel import select, or_, func
from sqlalchemy.orm import joinedload

# Importa las clases de tu aplicación
from bvirtual.models.auth.auth_models import UserInfo, User_Role
# Importa la clase del estado que quieres actualizar
from bvirtual.states.users.users_state import UserInfoState

class EditUserState(rx.State):
    """State for editing an existing user."""

    role_name: str = ""  # El nombre del rol seleccionado
    all_role_names: list[str] = []  # Lista de nombres de roles

    # Mensajes de estado
    edit_error: str = ""

    def load_roles(self):
        """Load roles from the database."""
        with rx.session() as session:
            self.all_role_names = session.exec(select(User_Role.name)).all()

    @rx.event
    def set_role_name(self, role: str):
        self.role_name = role
         
    @rx.event
    def handle_submit(self, form_data: dict[str, Any]):

        # Asegura que los campos booleanos estén presentes en form_data
        if 'is_admin' in form_data:
            form_data['is_admin'] = True
        else:
            form_data['is_admin'] = False

        if 'enabled' in form_data:
            form_data['enabled'] = True
        else:
            form_data['enabled'] = False

        # Validaciones
        if not form_data['name']:
            yield rx.toast.error("El nombre de usuario no puede estar vacio", duration=5000, position="top-center",)
            return

        if not form_data['email']:
            yield rx.toast.error("El correo no puede estar vacio", duration=5000, position="top-center",)
            return
      
        try:

            with rx.session() as session:
                # Carga el usuario a editar
                user_info = session.exec(
                    select(UserInfo)
                    .options(joinedload(UserInfo.localuser), joinedload(UserInfo.user_role))
                    .where(UserInfo.email == form_data['email'])
                ).one_or_none()

                if not user_info:
                    yield rx.toast.error("Usuario no encontrado.", duration=5000, position="top-center")
                    return

                # Actualiza los campos del usuario
                user_info.name = form_data['name']
                user_info.email = form_data['email']
                user_info.phone = form_data['phone']
                user_info.is_admin = form_data['is_admin']
                user_info.localuser.enabled = form_data['enabled']

                if self.role_name:
                    role = session.exec(select(User_Role).where(User_Role.name == self.role_name)).one_or_none()
                    if role:
                        user_info.user_role = role

                session.add(user_info)
                session.commit()

            # Recarga la lista de usuarios en UserInfoState
            yield UserInfoState.list_users()
            yield rx.toast.success("Usuario actualizado con éxito.", duration=5000, position="top-right")
            
        except Exception as e:
            print("Error updating user:", e)
            yield rx.toast.error("Error al actualizar el usuario.", duration=5000, position="top-center")
        