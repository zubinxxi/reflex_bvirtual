import reflex as rx
import reflex_local_auth

from bvirtual.template import template
from bvirtual.components.groups.list_groups import loading_table_groups

@rx.page(route="/grupos", title="Grupos | Biblioteca Virtual")
@template
@reflex_local_auth.require_login
def grupos() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Gestión de Grupos (Roles)", 
                size="4", 
                font_family="Staatliches",
                letter_spacing="2px",
            ),
            width="100%",
        ),
        loading_table_groups(),
        padding_y="20px",
        width="100%",
        
    )