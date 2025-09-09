import re
from typing import Any
import reflex as rx 
from sqlmodel import select
import reflex_local_auth

# model
from reflex_local_auth.user import LocalUser

class ChangePassword(reflex_local_auth.LocalAuthState):

    """Estado para manejar el cambio de contraseña."""

    # Variables de estado para el formulario
    old_password: str
    new_password: str
    confirm_password: str

    #función para validar la nueva contraseña
    def validate_new_password(self, new_password: str, confirm_password: str):
        if new_password != confirm_password:
            return rx.toast.error("Las nuevas contraseñas no coinciden.", duration="5000", position="top-center")
        if len(new_password) < 8:
            return rx.toast.error("La nueva contraseña debe tener al menos 8 caracteres.", duration="5000", position="top-center")
        if not re.search(r"[A-Z]", new_password):
            return rx.toast.error("La nueva contraseña debe tener al menos una mayúscula.", duration="5000", position="top-center")
        if not re.search(r"[a-z]", new_password):
            return rx.toast.error("La nueva contraseña debe tener al menos una minúscula.", duration="5000", position="top-center")
        if not re.search(r"\d", new_password):
            return rx.toast.error("La nueva contraseña debe tener al menos un número.", duration="5000", position="top-center")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", new_password):
            return rx.toast.error("La nueva contraseña debe tener al menos un carácter especial.", duration="5000", position="top-center")
        
        return None # Retorna None si las validaciones son exitosas
 
    @rx.event
    def handle_submit(self, form_data: dict[str, Any]):

        """Maneja el envío del formulario de cambio de contraseña."""
        self.old_password = form_data["old_password"]
        self.new_password = form_data["new_password"]
        self.confirm_password = form_data["confirm_password"]

        # Validar las nuevas contraseñas y capturar el resultado
        validation_result = self.validate_new_password(self.new_password, self.confirm_password)
        if validation_result:
            yield validation_result
            return

        # Lógica para cambiar la contraseña
        try:
            with rx.session() as session:
                # Busca el usuario actual en la base de datos
                current_user = session.exec(
                    select(LocalUser).where(LocalUser.id == self.authenticated_user.id)
                ).one_or_none()

                if not current_user:
                    yield rx.toast.error("Usuario no encontrado.", duration="5000", position="top-center")
                    return
                
                # Usa el método `verify()` de la instancia del usuario para verificar la contraseña
                if not current_user or not current_user.verify(self.old_password):
                    yield rx.toast.error("La contraseña actual es incorrecta", duration="5000", position="top-center")
                    return
                
                # Genera el nuevo hash de la contraseña usando el método `hash_password()`
                hashed_password = current_user.hash_password(self.new_password)

                # Actualiza la contraseña
                current_user.password_hash = hashed_password
                session.add(current_user)
                session.commit()
                session.refresh(current_user)

                # Redirige al usuario a la página de login
                yield rx.redirect("/") # Asume que la página de login está en la ruta principal "/" 

                # Cierra la sesión del usuario
                yield reflex_local_auth.LocalAuthState.do_logout            

                yield rx.toast.success("Contraseña actualizada con éxito.", duration="5000", position="top-right")
                self.reset() # Limpia los campos del formulario

        except Exception as e:
            print(f"Error al cambiar la contraseña: {e}")
            yield rx.toast.error(f"Error al cambiar la contraseña: {str(e)}", duration="5000", position="top-center")