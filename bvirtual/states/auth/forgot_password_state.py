import re
import reflex as rx 
import random
import string
import reflex_local_auth
from typing import Any, Optional
from sqlmodel import select

from bvirtual.email_utils import send_password_reset_email

# model
from reflex_local_auth.user import LocalUser
from bvirtual.models.auth.auth_models import UserInfo

# Components
from bvirtual.components.utils.messages import alert_success

class ForgotPasswordState(rx.State):
    """Estado para manejar la recuperación de contraseña"""

    #ser_name: str
    error_message: str = ""
    success_message: str = ""
    show_success_alert: bool = False
    show_error_alert: bool = False

    @rx.event
    def set_show_success_alert(self, value: bool):
        self.show_success_alert = value

    @rx.event
    def set_show_error_alert(self, value: bool):
        self.show_error_alert = value

    def generate_random_password(self, length: int = 12) -> str:
        """Genera una contraseña aleatoria y segura."""
        characters = string.ascii_letters + string.digits + string.punctuation
        new_password = ''.join(random.choice(characters) for i in range(length))
        return new_password
    
    def handle_submit(self, form_data: dict[str, Any]):
        """
        Maneja la lógica de restablecer la contraseña cuando se envía el formulario.
        """
        username = form_data["username"]
        
        self.error_message = ""
        self.success_message = ""

        if not username:
            self.error_message = "Por favor, ingresa tu usuario."
            yield rx.toast.error(self.error_message, duration="5000", position="top-center")
            return
        
        with rx.session() as session:
            # 1. Buscar al usuario por el nombre de usuario.
            user = session.exec(
                select(LocalUser).where(LocalUser.username == username)
            ).one_or_none()

            if not user:
                self.error_message = "No se encontró el usuario. Revisa que esté escrito correctamente."
                yield rx.toast.error(self.error_message, duration="5000", position="top-center")
                return

            # 2. Buscar la información adicional del usuario para obtener el email.
            user_info = session.exec(
                select(UserInfo).where(UserInfo.user_id == user.id)
            ).one_or_none()
            
            if not user_info or not user_info.email:
                self.error_message = "No se pudo encontrar un correo asociado a tu cuenta."
                yield rx.toast.error(self.error_message, duration="5000", position="top-center")
                return

            # 3. Generar una nueva contraseña y actualizar el modelo LocalUser.
            new_password = self.generate_random_password()
            user.password_hash = user.hash_password(new_password)
            session.add(user)
            session.commit()

            # 4. Enviar el correo electrónico con la nueva contraseña.
            if send_password_reset_email(user_info.email, new_password):
                self.success_message = "Se ha enviado un correo con tu nueva contraseña. Revisa tu bandeja de entrada."
                self.show_success_alert = True # <--- Cambia el estado de la alerta
            else:
                self.error_message = "Hubo un error al enviar el correo. Por favor, intenta de nuevo más tarde."
                self.show_error_alert = True # <--- Cambia el estado de la alerta
