import reflex as rx 

# States
from bvirtual.states.groups.edit_group_state import EditGroupState

# Model
from bvirtual.models.auth.auth_models import User_Role

def edit_group_button(group: User_Role) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.tooltip(
                    rx.hstack(
                        rx.icon("pencil", size=18),
                    ),
                    content="Actualizar Grupo",
                ),
                color_scheme="blue",
                variant="surface",
                size="1",
                on_click=lambda: EditGroupState.get_groups(group),
            ),
            
        ),

        rx.dialog.content(
            rx.dialog.title(
                "Actualizar Grupo",
            ),

            rx.dialog.description(
                "Actualize los datos del grupo",
            ),

            rx.form(
                rx.flex(                    
                    rx.input(
                        name="name",
                        placeholder="Grupo",
                        auto_focus=True,
                        spell_check=True,
                        type="text",
                        default_value=group.name,
                    ),

                    rx.input(
                        name="description",
                        placeholder="Descripción del grupo",
                        type="text",
                        default_value=group.description,
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

                on_submit=EditGroupState.handle_submit,
                reset_on_submit=False,
            ),
            max_width="450px",
        ),
    )
    