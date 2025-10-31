import reflex as rx 

# Model
from bvirtual.models.categorys.categorys_models import Categorys

# State
from bvirtual.states.categorys.del_category_state import DeleteCategorysState

def delete_category_button(category: Categorys) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.tooltip(
                    rx.hstack(
                        rx.icon("trash-2", size=18),
                    ),
                    content="Borrar Categoría",
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
                    rx.text(f"Eliminar la categoría: {category.description}",),

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
                        on_click=DeleteCategorysState.delete_categorys(category),
                    ),
                ),

                spacing="3",
                justify="end",
            ),

            max_width="450px",
        ),
    )