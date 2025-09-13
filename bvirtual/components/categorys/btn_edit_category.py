import reflex as rx 

# States
from bvirtual.states.categorys.edit_category_state import EditCategoryState

# Model
from bvirtual.models.categorys.categorys_models import Categorys

def edit_category_button(category: Categorys) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.tooltip(
                    rx.hstack(
                        rx.icon("pencil", size=18),
                    ),
                    content="Actualizar Categoría",
                ),
                color_scheme="blue",
                variant="surface",
                size="1",
                on_click=lambda: EditCategoryState.get_category(category),
            ),
            
        ),

        rx.dialog.content(
            rx.dialog.title(
                "Actualizar Categoría",
            ),

            rx.dialog.description(
                "Actualiz el nombre de la categoría",
            ),

            rx.form(
                rx.flex(
                    rx.input(
                        name="description",
                        placeholder="Descripción de la categoría",
                        type="text",
                        default_value=category.description,
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

                on_submit=EditCategoryState.handle_submit,
                reset_on_submit=False,
            ),
            max_width="450px",
        ),
    )
    