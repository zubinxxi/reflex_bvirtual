import reflex as rx
import re # Importa la librería re para expresiones regulares
from sqlmodel import select
from typing import Any, Optional
#from reflex_local_auth.user import LocalUser
from reflex_local_auth import RegistrationState
from bvirtual.states.users.users_state import UserInfoState
from bvirtual.models.auth.auth_models import UserInfo, User_Role

class AddUserState(RegistrationState):
    """State for adding a new user."""
    
    is_admin: bool = False
    email: str = ""
    phone: str = ""
    name: str = ""
    username: str = ""
    password: str = ""
    confirm_password: str = ""
    role_name: str = "" # El nombre del rol seleccionado
    all_role_names: list[str] = [] # Lista de nombres de roles

    # Mensajes de estado
    registration_error: str = ""

    
    def load_roles(self):
        """Load roles from the database."""
        with rx.session() as session:
            self.all_role_names = session.exec(select(User_Role.name)).all()

    """@rx.event
    def set_is_admin(self, admin: bool):
        self.sw_is_admin = admin"""

    @rx.event
    def set_role_name(self, role: str):
        self.role_name = role

    @rx.event
    def handle_submit(self, form_data: dict[str, Any]):
        # Patrón de expresión regular para un correo electrónico
        # Esta es una versión simplificada pero efectiva.
        EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        self.username = form_data['username']
        self.name = form_data['name']
        self.email = form_data['email']
        self.phone = form_data['phone']
        self.password = form_data['password']
        self.confirm_password = form_data['confirm_password']
        #print("Form Data:", form_data)  # Debugging line to print form data

        # Asegura que los campos booleanos estén presentes en form_data
        if 'is_admin' in form_data:
            #form_data['is_admin'] = True
            self.is_admin = True
        else:
            #form_data['is_admin'] = False
            self.is_admin = False

        """Validaciones"""
        if form_data['password'] != form_data['confirm_password']:
            yield rx.toast.error('Las contraseñas no coinciden.', duration=5000, position="top-center",)
            return
        
        if not form_data['password']:
            yield rx.toast.error('La contraseña no puede estar vacia', duration=5000, position="top-center",)
            return
        
        if not self.role_name:
            yield rx.toast.error("Debe seleccionar un rol.", duration=5000, position="top-center")
            return
        
        # Nueva validación de correo electrónico
        if not re.fullmatch(EMAIL_REGEX, self.email):
            yield rx.toast.error('Por favor, introduce un correo electrónico válido.', duration=5000, position="top-center")
            return

        
        try:
            """Primero inserta en la tabla localuser"""
            registration_result = self.handle_registration(form_data)

            """ Confirmo que se creo el usuario en localuser y luego inserto en userinfo """
            if self.new_user_id is not None:

                # Obtener el ID del rol a partir del nombre
                with rx.session() as session:
                    selected_role = session.exec(
                        select(User_Role).where(User_Role.name == self.role_name)
                    ).first()
                    if not selected_role:
                        self.registration_error = "Debe seleccionar un rol de la lista."
                        yield rx.toast.error(f"{self.registration_error}", duration=5000, position="top-center")
                        return

                    # Insertar en UserInfo
                    session.add(
                        UserInfo(
                            email=self.email,
                            user_id=self.new_user_id,
                            role_id=selected_role.id,
                            name=self.name.title(),
                            phone=self.phone,
                            is_admin=self.is_admin,
                        )
                    )
                    session.commit()
                    # Reset form fields
                    self.email = ""
                    self.phone = ""
                    self.name = ""
                    self.username = "" 
                    self.password = ""
                    self.confirm_password = ""
                    self.is_admin = False 
                    self.role_name = ""

                """Actualizar la lista de usuarios en UserInfoState"""
                yield UserInfoState.list_users()

            yield rx.toast.success(f"Usuario \"{form_data['name'].title()}\" creado con ¡ÉXITO!", duration=5000, position="top-right")
            
        
        except Exception as e:
            print("Error:", str(e))
            yield rx.toast.error(f"Error al crear el usuario: {str(e)}", duration=5000, position="top-center")
            

        