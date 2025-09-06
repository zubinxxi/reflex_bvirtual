import reflex as rx
import reflex_local_auth

from bvirtual.components.auth.marca import marca
from bvirtual.components.auth.form_login import form_login

@rx.page(
    route="/login",
    title="Login | Biblioteca Virtual",
)
def login() -> rx.Component:
    return rx.box(
        rx.color_mode.button(position="top-right"),

        rx.desktop_only(
            rx.hstack(
                rx.box(marca(), width="70%"),
                rx.box(form_login(),width="30%"),
                width="100%",
            ),
            width="100%",
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.box(marca(), width="100%"),
                rx.box(form_login(),width="100%"),
                width="100%",
            ),
            width="100%",
        ),
    )