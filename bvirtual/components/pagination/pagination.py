import reflex as rx 

def pagination_controls(
        set_limit: str, 
        prev_page: str, 
        page_number: str, 
        total_pages: str, 
        next_page:str, 
        total_items: str
    ) -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.hstack(
                rx.text("Ver"),
                rx.select(
                    ["5", "10", "25", "50"],
                    default_value = "10",
                    on_change = lambda value: set_limit(value),
                    size="1",
                    width="70px",
                ),
                rx.text("entradas"),
                width="20%",
                align="center",
                justify="start",
            ),

            rx.hstack(
                rx.button(
                    "Anterior",
                    on_click=prev_page,
                    variant="surface",
                    size="1",
                ),
                rx.text(
                    f"Page {page_number} / {total_pages}"
                ),
                rx.button(
                    "Siguiente",
                    on_click=next_page,
                    variant="surface",
                    size="1",
                ),
                width="60%",
                align="center",
                justify="center",
            ),
    
            rx.hstack(
                rx.text(f"Total de grupos: {total_items}"),
                width="20%",
                align="center",
                justify="end",
            ),

            width="100%",
            padding_x="10px",
            align="center",
            justify="between",
        ),
        justify="center",
        width="100%",
    ),

