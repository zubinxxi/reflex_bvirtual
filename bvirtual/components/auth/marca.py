import reflex as rx 

def marca() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.heading(
                    "Biblioteca Virtual", 
                    size="8", 
                    color="#FFF",
                ),

                rx.link(
                    rx.text(
                        "Documentación >>",
                        font_weight="bold",
                    ),
                ),

                background="url('/img/bg01.jpeg') no-repeat center center",
                height="100vh",
                align="center",
                justify="center",
                spacing="0",
            ),
        ),

        rx.mobile_and_tablet(
            rx.vstack(
                rx.heading(
                    "Biblioteca Virtual", 
                    size="8", 
                    color="#FFF",
                ),

                rx.link(
                    rx.text(
                        "Documentación >>",
                    ),
                ),

                background="url('/img/bg01.jpeg') no-repeat center center",
                height="30vh",
                align="center",
                justify="center",
                spacing="0",
            ),
            width="100%",
        ),

        width="100%",
    )
    