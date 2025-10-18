import reflex as rx 

# State
from bvirtual.states.state import MenuItemsStates


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def menu_category() -> rx.Component:

    return rx.hstack(
        rx.foreach(
            MenuItemsStates.categorys,
            lambda category:navbar_link(
                category.description,
                '#',
            ),
        ),
        width='100%',
        height="50px",
        justify='center',
        align='center',
        spacing='6',
        bg=rx.color("teal"),
    )