import reflex as rx 

# Model
from bvirtual.models.documents.document_models import Documents

# State
from bvirtual.states.documents.del_document_state import DeleteDocumentState

def delete_document_button(document: Documents) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.tooltip(
                    rx.hstack(
                        rx.icon("trash-2", size=18),
                    ),
                    content="Borrar Documento",
                ),
                color_scheme="tomato",
                variant="surface",
                size="1",
            ),
        ),

        rx.dialog.content(
            rx.dialog.title(
                "Eliminar",
            ),

            rx.dialog.description(
                rx.hstack(
                    rx.icon("trash-2",size=30, color="tomato"),
                    rx.text(f"Eliminar el documento: {document.name}",),

                    align="center",
                    justify="start",
                ),
            ),

            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "Cancelar",
                        variant="soft",
                        color_scheme="gray",
                    ),
                ),
                rx.dialog.close(
                    rx.button(
                        "Sí, eliminar",
                        type="submit",
                        variant="soft",
                        color_scheme="tomato",
                        on_click=DeleteDocumentState.delete_document(document),
                    ),
                ),

                spacing="3",
                justify="end",
            ),

            max_width="450px",
        ),
    )