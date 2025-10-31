import reflex as rx 
import reflex_local_auth

# Template
from bvirtual.template import template

# Componente
from bvirtual.components.auth.change_password import change_password

@rx.page(route="/cambiar-password", title="Cambiar Contraseña | Biblioteca Virtual")
@template
@reflex_local_auth.require_login
def change_password() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Cambiar Contraseña", 
                size="4", 
                font_family="Staatliches",
                letter_spacing="2px",
            ),
            width="100%",
        ),
        change_password(),
        padding_y="20px",
        width="100%",
    )
