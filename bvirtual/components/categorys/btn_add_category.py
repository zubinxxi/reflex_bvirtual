import reflex as rx

# State
from bvirtual.states.categorys.add_category_state import AddCategoryState

"""Funcion que maneja el formulario para agregar una nueva categoría"""
def add_category_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.tooltip(
                    rx.hstack(
                        rx.icon("plus", size=18),
                        rx.text("Nuevo", size="4"),
                        align="center",
                        justify="center",
                    ),
                    content="Crear Categoría",
                ),
                color_scheme="cyan",
                variant="surface",
            ),
        ),

        rx.dialog.content(
            rx.dialog.title(
                "Agregar Nueva Categoría",
            ),

            rx.dialog.description(
                "Agregue categorías al sistema",
            ),

            rx.form(
                rx.flex(
                    rx.input(
                        name="description",
                        placeholder="Descripción de la categoría",
                        type="text",
                        default_value=AddCategoryState.description,
                        text_transform="capitalize",
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
                                "Guardar",
                                type="submit",
                                variant="soft",
                            ),
                        ),

                        spacing="3",
                        justify="end",
                    ),

                    direction="column",
                    spacing="4",
                    margin_top="15px",
                ),

                on_submit=AddCategoryState.handle_submit,
                reset_on_submit=True,
            ),
            max_width="450px",
        ),
    )