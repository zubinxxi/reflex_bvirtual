import reflex as rx

# State
from bvirtual.states.state import MyLocalAuthState
#from reflex_local_auth import LocalAuthState



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
                        src="/img/logo.png",
                        width="12em",
                        height="auto",
                    ),
                    justify="start",
                    width="10%",
                ),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("About", "/#"),
                    navbar_link("Contact", "/#"),
                    spacing="5",
                    justify="center",
                    width="80%",
                ),
                rx.hstack(
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
                    width="10%",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/img/logo.png",
                        width="12em",
                        height="auto",
                        #border_radius="25%",
                    ),
                    #rx.heading(
                    #    "Reflex", size="6", weight="bold"
                    #),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        #rx.menu.item("Pricing"),
                        rx.menu.item("Contact"),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        #rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )