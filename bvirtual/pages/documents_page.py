import reflex as rx 
import reflex_local_auth

from bvirtual.template import template

from bvirtual.components.documents.list_documents import loading_table_documents

@rx.page(route="/documentos", title="Documentos | Biblioteca Virtual")
@template
@reflex_local_auth.require_login
def documents() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Documentos", 
                size="4", 
                font_family="Staatliches",
                letter_spacing="2px",
            ),
            width="100%",
        ),
        loading_table_documents(),
        padding_y="20px",
        width="100%",
        
    )