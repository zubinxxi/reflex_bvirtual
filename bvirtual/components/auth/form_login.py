import reflex as rx

import reflex_local_auth
#from bvirtual.states.auth_state import AuthState

def login_error() -> rx.Component:
    """Render the login error message."""
    return rx.cond(
        reflex_local_auth.LoginState.error_message != "",
        rx.callout(
            "Usuaorio o contraseña incorrectos",#reflex_local_auth.LoginState.error_message,
            icon="triangle_alert",
            color_scheme="red",
            role="alert",
            width="100%",
        ),
    )

def form_login() -> rx.Component: 
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.image(
                    src="/img/logo01.png",
                    width="auto",
                    height="auto",
                ),
                rx.heading(
                    "Por favor ingresa tu cuenta",
                    size="4",
                ),
                login_error(),

                rx.form(
                    rx.vstack(
                        rx.input(
                            rx.input.slot(rx.icon("user")),
                            placeholder="Usuario",
                            name="username",
                            variant="soft",
                            width="100%",
                            auto_focus=True,
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("lock")),
                            placeholder="Contraseña",
                            name="password",
                            type="password",
                            variant="soft",
                            width="100%",
                        ),
                        #rx.hstack(
                        #    rx.link("Restablecer contraseña", underline="none", href="/forgot-password"),
                        #),
                        rx.button(
                            "Iniciar Sesión",
                            type="submit",
                            width="100%",
                        ),

                        rx.hstack(
                            rx.link("Restablecer contraseña", underline="none", href="/forgot-password"),
                        ),

                        #rx.mobile_only(
                        #    rx.vstack(
                        #        rx.text("¿Eres nuevo aquí?"),
                        #        rx.link("Registrate", underline="none", href="/registro"),
                        #        spacing="2",
                        #    ),
                        #), 
                        #rx.tablet_and_desktop(
                        #    rx.hstack(
                        #        rx.text("¿Eres nuevo aquí?"),
                        #        rx.link("Registrate", underline="none", href="/registro"),
                        #        spacing="2",
                        #    ),
                        #),

                        spacing="5",
                    ),

                    on_submit=reflex_local_auth.LoginState.on_submit,  # Use the do_login method from reflex_local_auth
                ),

                height="100vh",
                justify="center",
                spacing="6",
                padding="40px",

            ),
        ),

        rx.mobile_and_tablet(
            rx.vstack(
                rx.image(
                    src="/img/logo.png",
                    width="auto",
                    height="auto",
                ),
                rx.heading(
                    "Por favor ingresa tu cuenta",
                    size="4",
                ),

                login_error(),

                rx.form(
                    rx.vstack(
                        rx.input(
                            rx.input.slot(rx.icon("user")),
                            placeholder="Usuario",
                            name="username",
                            variant="soft",
                            width="100%",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("lock")),
                            placeholder="Contraseña",
                            name="password",
                            type="password",
                            variant="soft",
                            width="100%",
                        ),
                        rx.hstack(
                            rx.link("Restablecer contraseña", underline="none", href="/forgot-password"),
                        ),
                        rx.button(
                            "Iniciar Sesión",
                            type="submit",
                            width="100%",
                        ),
                        rx.hstack(
                            rx.text("¿Eres nuevo aquí?"),
                            rx.link("Registrate", underline="none", href="/registro"),
                            spacing="2",
                        ),

                        spacing="5",
                    ),

                    on_submit=reflex_local_auth.LoginState.on_submit,  # Use the do_login method from reflex_local_auth
                ),

                justify="start",
                spacing="6",
                padding="20px",

            ),

            padding="20px",
        ),

        width="100%",
    )


