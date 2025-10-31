import reflex as rx 
import reflex_local_auth

from bvirtual.template import template
from bvirtual.components.documents.add_document import form_add_document

@rx.page(route="/agregar-documento", title="Agregar Documento | Biblioteca Virtual")
@template
@reflex_local_auth.require_login
def add_document() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Agregar Documento", 
                size="4", 
                font_family="Staatliches",
                letter_spacing="2px",
            ),
            width="100%",
        ),
        form_add_document(),
        padding_y="20px",
        width="100%",
        
    )