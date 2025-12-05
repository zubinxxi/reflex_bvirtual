import reflex as rx 


#models
from bvirtual.models.documents.document_models import Documents

# State
from bvirtual.states.state import IndexState

def show_document(documents: Documents) -> rx.Component:
    pass

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

                border_right=f"1px solid {rx.color('cyan')}",

                width='15%',
                height="80vh",
                padding_right='20px',
            ),

            rx.vstack(
                rx.text("Documentos: ", size="5", weight='bold', color=rx.color("teal")),
                rx.grid(
                    rx.foreach(
                        IndexState.documents, 
                        lambda documents: rx.dialog.root(
                                rx.dialog.trigger(
                                    rx.button(
                                        rx.tooltip(
                                            rx.image(
                                                src=f"{rx.get_upload_url(documents.name)}"
                                            ),
                                            content="Ver PDF",
                                        ),
                                        color_scheme="tomato",
                                        height="100%",
                                        variant="ghost",
                                    ),
                                    
                                ),

                                rx.dialog.content(
                                    rx.dialog.title(
                                        documents.name,
                                    ),

                                    rx.html(
                                        f"""
                                        <iframe 
                                            src="{rx.get_upload_url(documents.name)}" 
                                            width="100%" 
                                            height="800px"
                                            style="border: 1px solid #e0e0e0; border-radius: 8px;"
                                        >
                                        </iframe>
                                        """,
                                        width="100%",
                                    ),

                                    max_width="700px",
                                    height="900px",
                                ),
                            ),
                    ),
                    columns="3",
                    spacing="4",
                    width="100%",
                ),
                width='90%',
                align='center',
                height="80vh",
            ),

            justify='center',
            #border='1px solid #e0e0e0',
            padding="20px",
        ),

        on_mount=IndexState.list_documents,
        width='100%',        
        align='center',
        padding="20px",
    )