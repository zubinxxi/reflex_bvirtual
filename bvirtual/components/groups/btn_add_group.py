import reflex as rx

# State
from bvirtual.states.groups.add_group_state import AddGroupState

"""Funcion que maneja el formulario para agregar un nuevo grupo"""
def add_group_button() -> rx.Component:
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
                    content="Crear Grupo",
                ),
                color_scheme="cyan",
                variant="surface",
            ),
        ),

        rx.dialog.content(
            rx.dialog.title(
                "Agregar Nuevo Grupo",
            ),

            rx.dialog.description(
                "Agregue grupos al sistema",
            ),

            rx.form(
                rx.flex(
                    rx.input(
                        name="name",
                        placeholder="Escriba el nombre",
                        type="text",
                        default_value=AddGroupState.name,
                        spell_check=True,
                        text_transform="uppercase",
                    ),

                    rx.input(
                        name="description",
                        placeholder="Descripción del grupo",
                        type="text",
                        default_value=AddGroupState.description,
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

                on_submit=AddGroupState.handle_submit,
                reset_on_submit=True,
            ),
            max_width="450px",
        ),
    )