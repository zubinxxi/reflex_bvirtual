import reflex as rx 
import reflex_local_auth

from bvirtual.template import template
from bvirtual.components.categorys.list_categorys import loading_table_categorys

@rx.page(route="/categorias", title="Categorías | Biblioteca Virtual")
@template
@reflex_local_auth.require_login
def categorys() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Gestión de Categorías", 
                size="4", 
                font_family="Staatliches",
                letter_spacing="2px",
            ),
            width="100%",
        ),
        loading_table_categorys(),
        padding_y="20px",
        width="100%",
        
    )