from typing import Any
import reflex as rx 

def alert_success(title: str, message: str, is_open: rx.Var[bool], on_ok_click: Any) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.alert_dialog.title(
                rx.vstack(
                    rx.icon("circle-check-big", color="green", size=60,),
                    title, 
                    align="center",
                    justify="center", 
                    width="100%",
                )
            ),
            rx.alert_dialog.description(
                rx.hstack(
                    rx.text(message),
                    align="center",
                    justify="center", 
                    width="100%",
                ),
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.hstack(
                        rx.button("OK", on_click=on_ok_click),
                        justify="center", 
                        width="100%",
                    )
                ),
                spacing="3",
            ),
        ),
        open=is_open,
    ),

def alert_error(title: str, message: str, is_open: rx.Var[bool], on_ok_click: Any) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.alert_dialog.title(
                rx.vstack(
                    rx.icon("ban", color="tomato", size=60,),
                    title, 
                    align="center",
                    justify="center", 
                    width="100%",
                )
            ),
            rx.alert_dialog.description(
                rx.hstack(
                    rx.text(message),
                    align="center",
                    justify="center", 
                    width="100%",
                ),
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.hstack(
                        rx.button("OK", on_click=on_ok_click),
                        justify="center", 
                        width="100%",
                    )
                ),
                spacing="3",
            ),
        ),
        open=is_open,
    ),

def alert_info(title: str, message: str, is_open: rx.Var[bool], on_ok_click: Any) -> rx.Component:
    pass

def alert_warning(title: str, message: str, is_open: rx.Var[bool], on_ok_click: Any) -> rx.Component:
    pass