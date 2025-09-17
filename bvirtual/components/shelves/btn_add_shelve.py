import reflex as rx

# State
from bvirtual.states.shelves.add_shelve_state import AddShelveState

"""Funcion que maneja el formulario para agregar una nueva categoría"""
def add_shelve_button() -> rx.Component:
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
                    content="Crear Estante",
                ),
                color_scheme="cyan",
                variant="surface",
            ),
        ),

        rx.dialog.content(
            rx.dialog.title(
                "Agregar Nuevo Estante",
            ),

            rx.dialog.description(
                "Agregue estantes al sistema",
            ),

            rx.form(
                rx.flex(
                    rx.input(
                        name="description",
                        placeholder="Descripción del estante",
                        type="text",
                        default_value=AddShelveState.description,
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

                on_submit=AddShelveState.handle_submit,
                reset_on_submit=True,
            ),
            max_width="450px",
        ),
    )