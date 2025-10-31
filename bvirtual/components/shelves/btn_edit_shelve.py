import reflex as rx 

# States
from bvirtual.states.shelves.edit_shelve_state import EditShelveState

# Model
from bvirtual.models.shelves.shelves_models import Shelves

def edit_shelve_button(shelve: Shelves) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.tooltip(
                    rx.hstack(
                        rx.icon("pencil", size=18),
                    ),
                    content="Actualizar Estante",
                ),
                color_scheme="blue",
                variant="surface",
                size="1",
                on_click=lambda: EditShelveState.get_shelve(shelve),
            ),
            
        ),

        rx.dialog.content(
            rx.dialog.title(
                "Actualizar Estante",
            ),

            rx.dialog.description(
                "Actualiza el nombre del estante",
            ),

            rx.form(
                rx.flex(
                    rx.input(
                        name="description",
                        placeholder="Descripción de la categoría",
                        type="text",
                        default_value=shelve.description,
                        spell_check=True,
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

                on_submit=EditShelveState.handle_submit,
                reset_on_submit=False,
            ),
            max_width="450px",
        ),
    )
    