import reflex as rx


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
                        rx.input(
                            rx.input.slot(rx.icon("mail")),
                            placeholder="Email",
                            name="email",
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
                    "Por favor ingresa tu correo",
                    size="4",
                ),

                rx.form(
                    rx.vstack(
                        rx.input(
                            placeholder="Email",
                            name="email",
                            variant="soft",
                            width="100%",

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
                ),

                justify="start",
                spacing="6",
                padding="20px",

            ),

            padding="20px",
        ),

        width="100%",
    )


