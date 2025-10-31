import reflex as rx


def form_register() -> rx.Component: 
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.image(
                    src="/img/logo.png",
                    width="auto",
                    height="auto",
                ),
                rx.heading(
                    "Por favor ingresa tus datos",
                    size="4",
                ),

                rx.form(
                    rx.vstack(
                        rx.input(
                            placeholder="Usuario",
                            name="login",
                            variant="soft",
                            width="100%",
                        ),
                        rx.input(
                            placeholder="Nombre y Apellido",
                            name="name",
                            variant="soft",
                            width="100%",

                        ),
                        rx.input(
                            placeholder="Email",
                            name="email",
                            variant="soft",
                            width="100%",

                        ),
                        rx.input(
                            placeholder="Contraseña",
                            name="pswd",
                            type="password",
                            variant="soft",
                            width="100%",
                        ),
                        rx.input(
                            placeholder="Confirmar Contraseña",
                            name="pswd2",
                            variant="soft",
                            type="password",
                            width="100%",
                        ),
                        rx.button(
                            "Guardar",
                            type="submit",
                            width="100%",
                        ),
                        rx.hstack(
                            rx.text("¿Tienes una cuenta?"),
                            rx.link("Inicia Sesión", underline="none", href="/login"),
                            spacing="2",
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
                    "Por favor ingresa tu cuenta",
                    size="4",
                ),

                rx.form(
                    rx.vstack(
                        rx.input(
                            placeholder="Usuario",
                            name="login",
                            variant="soft",
                            width="100%",
                        ),
                        rx.input(
                            placeholder="Nombre y Apellido",
                            name="name",
                            variant="soft",
                            width="100%",

                        ),
                        rx.input(
                            placeholder="Email",
                            name="email",
                            variant="soft",
                            width="100%",

                        ),
                        rx.input(
                            placeholder="Contraseña",
                            name="pswd",
                            type="password",
                            variant="soft",
                            width="100%",
                        ),
                        rx.input(
                            placeholder="Confirmar Contraseña",
                            name="pswd2",
                            variant="soft",
                            type="password",
                            width="100%",
                        ),
                        rx.button(
                            "Guardar",
                            type="submit",
                            width="100%",
                        ),
                        rx.mobile_only(
                            rx.vstack(
                                rx.text("¿Tienes una cuenta?"),
                                rx.link("Inicia Sesión", underline="none", href="/login"),
                                spacing="2",
                            ),
                        ), 
                        rx.tablet_and_desktop(
                            rx.hstack(
                                rx.text("¿Tienes una cuenta?"),
                                rx.link("Inicia Sesión", underline="none", href="/login"),
                                spacing="2",
                            ),
                        ),   

                        spacing="5",
                    ),
                ),

                justify="start",
                spacing="6",
                padding="40px",

            ),

            padding="20px",
        ),

        width="100%",
    )


