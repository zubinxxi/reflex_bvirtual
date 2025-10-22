import reflex as rx 

# State
from bvirtual.states.state import IndexState

def document_section() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.input(
                placeholder="Buscar Documento...",
                on_change=lambda value: IndexState.set_search(value),
                width='50%'
            ),
            justify='center',
            align='center',
            width='100%',
            height='60px',
            margin_bottom='20px',
        ),

        rx.hstack(
            rx.vstack(
                rx.heading("Categorías"),
                # Selector de Categorías
                rx.select(
                    items=IndexState.all_category_names,
                    placeholder="Seleccionar",
                    #default_value=IndexState.category_name,
                    on_change=IndexState.set_category_name,
                    width="100%",
                ),

                rx.heading("Estantes"),
                # Selector de estantes
                rx.select(
                    items=IndexState.all_shelve_names,
                    placeholder="Seleccionar",
                    #default_value=IndexState.shelve_name,
                    on_change=IndexState.set_shelve_name,
                    width="100%",
                ),

                width='10%',
                margin_x='20px',
            ),
            rx.vstack(
                rx.text("Documentos: ", size="5", weight='bold', color=rx.color("teal")),
                width='90%',
                align='center',
                border='1px solid #e0e0e0',
            ),
            #spacing='8',
            justify='center',
            border='1px solid #e0e0e0',
        ),

        width='100%',
        align='center',
        padding="20px",
    )