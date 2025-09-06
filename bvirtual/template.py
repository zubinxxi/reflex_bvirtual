from typing import Callable
import reflex as rx

# Components
from bvirtual.components.layout.header import header
from bvirtual.components.layout.sidebar import sidebar


def template(
    page: Callable[[], rx.Component],
) -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        rx.desktop_only(
            rx.grid(
                sidebar(),
                rx.box(
                    header('Biblioteca Virtual'),
                    rx.box(
                        page(), # funcion que renderiza la pagina
                        height="90vh",
                        #margin_top="20px",
                        #border_radius="10px",
                    ),
                    padding_x="20px",
                ),
                grid_template_columns="16em 1fr",
                gap="4",
                width="100%",
            ),
        ),

        rx.mobile_and_tablet(
            sidebar(),
            rx.box(
                header('Dashboard'),
                rx.box(
                    page(), # funcion que renderiza la pagina                  
                    height="100vh",
                    #margin_top="20px",
                    border_radius="10px",
                ),
                padding_x="10px",
            ),
            gap="4",
            width="100%",
        ),
        
    )