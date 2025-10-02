import reflex as rx
from reflex.style import set_color_mode, color_mode

# State
from bvirtual.states.state import MyLocalAuthState
from bvirtual.states.state import MenuItemsStates
#from reflex_local_auth import LocalAuthState

def dark_mode_toggle() -> rx.Component:
    return rx.segmented_control.root(
        #rx.segmented_control.item(
        #    rx.icon(tag="monitor", size=20),
        #    value="system",
        #),
        rx.segmented_control.item(
            rx.icon(tag="sun", size=20),
            value="light",
        ),
        rx.segmented_control.item(
            rx.icon(tag="moon", size=20),
            value="dark",
        ),
        on_change=set_color_mode,
        variant="classic",
        radius="large",
        value=color_mode,
    )


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar_buttons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/img/logo01.png",
                        width="12em",
                        height="auto",
                    ),
                    justify="start",
                    width="15%",
                ),
                rx.hstack(
                    navbar_link("Inicio", "/"),
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.button(
                                rx.text(
                                    "Categorías",
                                    size="4",
                                    weight="medium",
                                ),
                                rx.icon("chevron-down"),
                                weight="medium",
                                variant="ghost",
                                size="3",
                            ),
                        ),
                        rx.menu.content(
                            rx.foreach(
                                    MenuItemsStates.categorys,
                                    lambda category:rx.menu.item(
                                        category.description,
                                    ),
                                ),
                            
                        ),
                    ),
                    navbar_link("Acerca de", "/#"),
                    navbar_link("Contacto", "/#"),
                    spacing="5",
                    justify="center",
                    width="70%",
                ),
                rx.hstack(
                    dark_mode_toggle(),
                    rx.cond(
                        MyLocalAuthState.is_authenticated,
                        rx.menu.root(
                            rx.menu.trigger(
                                rx.button(
                                    rx.hstack(
                                        rx.icon('circle-user-round'),
                                        rx.text(f"{MyLocalAuthState.authenticated_user_info.name}", size="3"),
                                    ), 
                                    size="3"
                                ),
                            ),
                            rx.menu.content(
                                rx.menu.item(
                                    rx.link("Panel de Control", href="/panel", underline="none", width="100%"),
                                ),
                                rx.menu.separator(),
                                rx.menu.item(
                                    rx.link(
                                        'Cerrar Sesión',
                                        href="/",
                                        on_click=MyLocalAuthState.do_logout,
                                        underline="none",
                                        width="100%"
                                    )
                                ),
                            ),
                        ),
                        rx.link(
                            rx.button("Log In", size="3"),
                            href="/login",
                        ),

                    ),
                    
                    spacing="4",
                    justify="end",
                    width="15%",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/img/logo01.png",
                        width="12em",
                        height="auto",
                    ),
                    dark_mode_toggle(),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Inicio"),
                        rx.menu.item("About"),
                        rx.menu.item("Contact"),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        position="fixed",
        top="0px",
        z_index="5",
        width="100%",
    )