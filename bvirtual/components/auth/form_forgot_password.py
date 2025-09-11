import reflex as rx

# State
from bvirtual.states.auth.forgot_password_state import ForgotPasswordState


def form_forgot_password() -> rx.Component: 
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.image(
                    src="/img/logo01.png",
                    width="auto",
                    height="auto",
                ),
                rx.heading(
                    "Por favor ingresa tu correo",
                    size="4",
                ),

                rx.form(
                    rx.vstack(
                        rx.cond(
                            ForgotPasswordState.error_message != "",
                            rx.text(ForgotPasswordState.error_message, color="red"),
                        ),
                        rx.cond(
                            ForgotPasswordState.success_message != "",
                            rx.text(ForgotPasswordState.success_message, color="green"),
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("user")),
                            placeholder="Usuario",
                            name="username",
                            variant="soft",
                            width="100%",
                            auto_focus=True,
                        ),
                        rx.button(
                            "Restablecer",
                            type="submit",
                            width="100%",
                        ),

                        rx.tablet_and_desktop(
                            rx.hstack(
                                rx.text("¿Recordaste tu contraseña?"),
                                rx.link("Iniciar Sesión", underline="none", href="/login"),
                                spacing="2",
                            ),
                        ),

                        spacing="5",
                    ),
                    on_submit=ForgotPasswordState.handle_submit,
                    reset_on_submit=True,
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
                    src="/img/logo01.png",
                    width="auto",
                    height="auto",
                ),
                rx.heading(
                    "Por favor ingresa tu correo",
                    size="4",
                ),

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
                        rx.button(
                            "Iniciar Sesión",
                            type="submit",
                            width="100%",
                        ),

                        rx.mobile_only(
                            rx.vstack(
                                rx.text("¿Recordaste tu contraseña?"),
                                rx.link("Iniciar Sesión", underline="none", href="/login"),
                                spacing="2",
                            ),
                        ), 
                        rx.tablet_and_desktop(
                            rx.hstack(
                                rx.text("¿Recordaste tu contraseña?"),
                                rx.link("Iniciar Sesión", underline="none", href="/login"),
                                spacing="2",
                            ),
                        ),
                        spacing="5",
                    ),
                    on_submit=ForgotPasswordState.handle_submit,
                    reset_on_submit=True,
                ),

                justify="start",
                spacing="6",
                padding="20px",

            ),

            padding="20px",
        ),

        width="100%",
    )


