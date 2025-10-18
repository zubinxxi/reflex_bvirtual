import reflex as rx 

def hero() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.vstack(
                    rx.heading(
                        "Biblioteca Virtual", 
                        size="9", 
                        color=rx.color("teal"),
                        font_family="Staatliches",
                        letter_spacing="8px",
                        box_shadow="0px 0px 50px 0px #00bfc9",
                        margin_bottom="20px",
                        border_radius="10px",
                        text_align="center",
                        
                    ),
                    rx.text(
                        "Tu repositorio de documentos digitales de confianza.",
                        size="6",
                        color="#ccc",
                        font_weight="bold",
                        font_family="Nunito",
                        text_align="center",
                    ),
                    justify="center",
                    align="center",
                ),
                
                background_color="rgba(0, 0, 0, 0.5)",
                background_image="url('/img/library06.png')",
                background_size="cover",
                background_position="center",
                background_repeat="no-repeat",
                width="100%",
                height="60vh",
                #padding="2em",
                align="center",
                justify="center",
                
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.vstack(
                    rx.heading(
                        "Biblioteca Virtual", 
                        size="8", 
                        color=rx.color("teal"),
                        font_family="Staatliches",
                        letter_spacing="8px",
                        box_shadow="0px 0px 50px 0px #00bfc9",
                        margin_y="20px",
                        border_radius="10px",
                        text_align="center",
                        
                    ),
                    rx.text(
                        "Tu repositorio de documentos digitales de confianza.",
                        size="5",
                        color="#ccc",
                        font_weight="bold",
                        font_family="Nunito",
                        text_align="center",
                    ),
                    justify="center",
                    align="center",
                ),
                
                background_color="rgba(0, 0, 0, 0.5)",
                background_image="url('/img/library06.png')",
                background_size="cover",
                background_position="center",
                background_repeat="no-repeat",
                width="100%",
                height="50vh",
                padding="2em",
                align="center",
                justify="center",
                
            ),
        ),
    )