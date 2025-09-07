import reflex as rx 
import reflex_local_auth

# State
from bvirtual.states.auth.change_password_state import ChangePassword

def change_password() -> rx.Component:
    return rx.center(
        rx.box(
            rx.form(
                rx.vstack(
                    rx.heading("Cambiar Contraseña", size="5"),
                    rx.text("Ingresa tu contraseña actual y la nueva contraseña.", color="gray"),
                    
                    rx.input(
                        placeholder="Contraseña Actual",
                        type="password",
                        name="old_password",
                        is_required=True,
                    ),
                    rx.input(
                        placeholder="Nueva Contraseña",
                        type="password",
                        name="new_password",
                        is_required=True,
                    ),
                    rx.input(
                        placeholder="Confirmar Nueva Contraseña",
                        type="password",
                        name="confirm_password",
                        is_required=True,
                    ),
                    rx.button("Cambiar Contraseña", type="submit", width="100%"),
                    align="stretch",
                ),
                on_submit=ChangePassword.handle_submit,
                reset_on_submit=True,
            ),
            
            width="100%",
            max_width="400px",
            border="1",
        ),
        height="60vh",
    )