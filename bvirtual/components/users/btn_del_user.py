import reflex as rx 

from bvirtual.models.auth.auth_models import UserInfo
from bvirtual.states.users.del_user_state import DeleteUserState



def delete_user_button(user: UserInfo) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.tooltip(
                    rx.hstack(
                        rx.icon("trash-2", size=18),
                    ),
                    content="Borrar Usuario",
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
                    rx.text(f"Eliminar el usuario: {user.name}",),

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
                        on_click=DeleteUserState.delete_user(user),
                    ),
                ),

                spacing="3",
                justify="end",
            ),

            max_width="450px",
        ),
    )