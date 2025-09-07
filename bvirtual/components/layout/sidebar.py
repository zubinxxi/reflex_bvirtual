from typing import Optional
import reflex as rx 
from sqlmodel import select
import reflex_local_auth
#from bvirtual.states.auth_state import AuthState
from bvirtual.states.state import MyLocalAuthState
from reflex_local_auth import LocalAuthState


def sidebar_item_logout() -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon("log-out"),
            rx.text("Cerrar Sesión", size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
            },
        ),
        href="/login",
        on_click=LocalAuthState.do_logout,
        underline="none",
        weight="medium",
        width="100%",
        padding_x="0.4em",
    ),

def sidebar_item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
        padding_x="0.4em",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Dashboard", "layout-dashboard", "/"),
        sidebar_item("Documentos", "library", "/#"),
        rx.accordion.root(
            rx.accordion.item(
                header=rx.hstack(
                    rx.icon('briefcase-business'),
                    rx.text('Mantenimiento', size="4"),
                ),
                content=rx.vstack(
                    rx.link(
                        rx.hstack(rx.icon("list"), rx.text("Categorías"), align="center", justify="start"),
                        href="/categorias",    
                        underline="none",
                        trim="both",
                        width="100%",                        
                    ),
                    rx.link(
                        rx.hstack(rx.icon("square-library"), rx.text("Estantes"), align="center", justify="start"),
                        href="/estantes",    
                        underline="none",
                        trim="both",
                        width="100%",
                    ),
                    spacing="5",
                ),
            ),
            width="100%",
            #collapsible=True,
            type="multiple",
            orientation="vertical",
            variant="ghost",
        ),
        spacing="1",
        width="100%",
        font_family="Nunito",
    )

def settings_items() -> rx.Component:
    return rx.accordion.root(
        rx.accordion.item(
            header=rx.hstack(
                rx.icon('settings'),
                rx.text('Ajustes', size="4"),
            ),
            content=rx.vstack(
                rx.link(
                    rx.hstack(rx.icon("user"), rx.text("Usuarios"), align="center", justify="start"),
                    href="/usuarios",    
                    underline="none",
                    trim="both",
                    width="100%",                        
                ),
                rx.link(
                    rx.hstack(rx.icon("users"), rx.text("Grupos"), align="center", justify="start"),
                    href="/grupos",    
                    underline="none",
                    trim="both",
                    width="100%",
                ),
                rx.link(
                    rx.hstack(rx.icon("key-round"), rx.text("Cambiar Contraseña"), align="center", justify="start"),
                    href="/cambiar-password",    
                    underline="none",
                    trim="both",
                    width="100%",
                ),
                spacing="5",
            ),
        ),
        width="100%",
        #collapsible=True,
        type="multiple",
        orientation="vertical",
        variant="ghost",
    ),

def sidebar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.image(
                        src="/img/logo01.png",
                        width="100%",
                        height="auto",
                        border_radius="5px",
                    ),
                    align="center",
                    justify="start",
                    padding_x="0.5rem",
                    width="100%",
                    
                ),
                sidebar_items(),
                rx.spacer(),
                rx.vstack(
                    rx.vstack(
                        rx.cond(
                            MyLocalAuthState.authenticated_user_info.is_admin,
                            settings_items(),
                            rx.text(''),
                        ),
                        sidebar_item_logout(),
                        spacing="1",
                        width="100%",
                        font_family="Nunito",
                    ),
                    rx.divider(),
                    rx.hstack(
                        rx.icon_button(
                            rx.icon("user"),
                            size="3",
                            radius="full",
                        ),
                        rx.divider( orientation="vertical" ),
                        rx.vstack(
                            
                            rx.box(
                                rx.cond(
                                    MyLocalAuthState.authenticated_user_info,
                                    rx.text(MyLocalAuthState.authenticated_user_info.name, size="3", weight="bold",),
                                    rx.heading("Usuario no autenticado", size="3", weight="bold",),
                                ),
                                
                                rx.cond(
                                    MyLocalAuthState.authenticated_user_info,
                                    rx.text(MyLocalAuthState.authenticated_user_info.email,size="1"),
                                    rx.text("No email", size="1"),
                                ),
                                
                                width="100%",
                            ),
                            spacing="0",
                            align="start",
                            justify="start",
                            width="100%",
                        ),
                        padding_x="0.5rem",
                        align="center",
                        justify="start",
                        width="100%",
                        font_family="Raleway",
                    ),
                    width="100%",
                    spacing="5",
                ),
                spacing="5",
                # position="fixed",
                # left="0px",
                # top="0px",
                # z_index="5",
                padding_x="1em",
                padding_y="1.5em",
                bg=rx.color("accent", 3),
                align="start",
                # height="100%",
                height="100vh",
                width="16em",
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=30)
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("x", size=30)
                                ),
                                width="100%",
                            ),
                            rx.image(
                                src="/img/logo.png",
                                width="auto",
                                height="auto",
                                border_radius="5px",
                            ),
                            sidebar_items(),
                            rx.spacer(),
                            rx.vstack(
                                rx.vstack(
                                    settings_items(),
                                    sidebar_item_logout(),
                                    width="100%",
                                    spacing="1",
                                ),
                                rx.divider(margin="0"),
                                rx.hstack(
                                    rx.icon_button(
                                        rx.icon("user"),
                                        size="3",
                                        radius="full",
                                    ),
                                    rx.vstack(
                                        rx.box(
                                            rx.cond(
                                                MyLocalAuthState.authenticated_user_info,
                                                rx.text(MyLocalAuthState.authenticated_user_info.name, size="3", weight="bold",),
                                                rx.heading("Usuario no autenticado", size="3", weight="bold",),
                                            ),
                                            
                                            rx.cond(
                                                MyLocalAuthState.authenticated_user_info,
                                                rx.text(MyLocalAuthState.authenticated_user_info.email,size="1"),
                                                rx.text("No email", size="1"),
                                            ),
                                            width="100%",
                                        ),
                                        spacing="0",
                                        justify="start",
                                        width="100%",
                                    ),
                                    padding_x="0.5rem",
                                    align="center",
                                    justify="start",
                                    width="100%",
                                ),
                                width="100%",
                                spacing="5",
                            ),
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg=rx.color("accent", 2),
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),

        
    )