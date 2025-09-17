import reflex as rx 

# Model
from bvirtual.models.shelves.shelves_models import Shelves

# State
from bvirtual.states.shelves.del_shelve_state import DeleteShelvesState

def delete_shelve_button(shelve: Shelves) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.tooltip(
                    rx.hstack(
                        rx.icon("trash-2", size=18),
                    ),
                    content="Borrar Estante",
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
                    rx.text(f"Eliminar el estante: {shelve.description}",),

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
                        on_click=DeleteShelvesState.delete_shelves(shelve),
                    ),
                ),

                spacing="3",
                justify="end",
            ),

            max_width="450px",
        ),
    )