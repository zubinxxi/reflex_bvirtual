from typing import Callable
import reflex as rx

from bvirtual.components.auth.marca import marca

def template_auth(
    page: Callable[[], rx.Component],
) -> rx.Component:
    return rx.box(
        rx.color_mode.button(position="top-right"),
        rx.desktop_only(
            rx.hstack(
                rx.box(marca(), width="70%"),
                rx.box(
                    page(), # funcion que renderiza la pagina,
                    width="30%"
                ),
                width="100%",
            ),
            width="100%",
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.box(marca(), width="100%"),
                rx.box(
                    page(), # funcion que renderiza la pagina
                    width="100%"
                ),
                width="100%",
            ),
            width="100%",
        ),
    )