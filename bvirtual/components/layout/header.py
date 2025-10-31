import reflex as rx 

def header (title: str) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading(
                title, 
                font_family="Staatliches", 
                letter_spacing="4px", 
                class_name="animate__animated animate__bounce",
            ),
            rx.color_mode.button(position="top-right"),
            justify="between",
            width="100%"
        ),
        rx.divider(),
        margin_top="25px",
        spacing="4",
    )