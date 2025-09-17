import reflex as rx 
import reflex_local_auth

from bvirtual.template import template

@rx.page(route="/estantes", title="Estantes | Biblioteca Virtual")
@template
@reflex_local_auth.require_login
def shelves() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Estantes", 
                size="4", 
                font_family="Staatliches",
                letter_spacing="2px",
            ),
            width="100%",
        ),
        #loading_table_shelves(),
        padding_y="20px",
        width="100%",
        
    )