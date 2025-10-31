import reflex as rx
import reflex_local_auth

from bvirtual.template import template
from bvirtual.components.users.list_users import loading_table_users

@rx.page(route="/usuarios", title="Usuarios | Biblioteca Virtual")
@template
@reflex_local_auth.require_login
def users() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Gestión de Usuarios", 
                size="4", 
                font_family="Staatliches",
                letter_spacing="2px",
            ),
            width="100%",
        ),
        loading_table_users(),
        padding_y="20px",
        width="100%",
        
    )