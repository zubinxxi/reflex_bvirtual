import reflex as rx 

# Model
from bvirtual.models.auth.auth_models import User_Role

# State
from bvirtual.states.groups.del_group_state import DeleteGroupState

def delete_group_button(group: User_Role) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.tooltip(
                    rx.hstack(
                        rx.icon("trash-2", size=18),
                    ),
                    content="Borrar Grupo",
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
                    rx.text(f"Eliminar el grupo: {group.name}",),

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
                        on_click=DeleteGroupState.delete_group(group),
                    ),
                ),

                spacing="3",
                justify="end",
            ),

            max_width="450px",
        ),
    )