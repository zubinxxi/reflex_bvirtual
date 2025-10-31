from typing import Callable
import reflex as rx

# Components
from bvirtual.components.index.navbar import navbar_buttons



def template_web(
    page: Callable[[], rx.Component],
) -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        navbar_buttons(),
        rx.desktop_only(
            rx.box(
                page(), # funcion que renderiza la pagina
                height="100vh",
                overflow_y="auto",
            ),
        ),

        rx.mobile_and_tablet(
            rx.box(
                page(), # funcion que renderiza la pagina
                height="92vh",
                overflow_y="auto",
            ),
        ),
        
    )