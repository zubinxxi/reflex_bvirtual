import reflex as rx
import reflex_local_auth

from bvirtual.template import template

# State
from bvirtual.states.state import MyLocalAuthState
from bvirtual.states.state import MenuItemsStates

# Components
from bvirtual.components.index.navbar import navbar_buttons

@rx.page(
    route="/", 
    title="Inicio | Biblioteca Virtual",
    on_load=MenuItemsStates.items_menu,
)
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