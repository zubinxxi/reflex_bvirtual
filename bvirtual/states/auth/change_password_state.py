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
 

    @rx.event
    def handle_submit(self, form_data: dict[str, Any]):

        """Maneja el envío del formulario de cambio de contraseña."""
        self.old_password = form_data["old_password"]
        self.new_password = form_data["new_password"]
        self.confirm_password = form_data["confirm_password"]

        # Validaciones
        if self.new_password != self.confirm_password:
            yield rx.toast.error("Las nuevas contraseñas no coinciden.", duration="5000", position="top-center")
            return

        if len(self.new_password) < 8:
            yield rx.toast.error("La nueva contraseña debe tener al menos 8 caracteres.", duration="5000", position="top-center")
            return

        # Verifica si el usuario está autenticado
        if not self.is_authenticated:
            yield rx.toast.error("Debes iniciar sesión para cambiar tu contraseña.", duration="5000", position="top-center")
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
                
                # Usa el método `verify()` de la instancia del usuario para verificar la contraseñ
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