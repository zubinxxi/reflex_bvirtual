import reflex as rx
import reflex_local_auth

from bvirtual.template import template

# State
from bvirtual.states.state import MyLocalAuthState

# Components
from bvirtual.components.index.navbar import navbar_buttons

@rx.page(route="/", title="Inicio | Biblioteca Virtual")
#@template
#@reflex_local_auth.require_login
def index() -> rx.Component:
    return rx.box(
        navbar_buttons(),
        rx.container(
            rx.vstack(
                

                spacing="5",
                justify="center",
                min_height="50vh",
            ),
        ),
    )