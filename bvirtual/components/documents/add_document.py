import reflex as rx 

# States
from bvirtual.states.documents.add_document_state import AddDocumentState

# Components
from bvirtual.components.files.upload import upload_document

color = "rgb(107,99,246)"

def form_add_document():

    return rx.box(
        rx.card(
            rx.hstack(
                rx.link(
                    rx.button(
                        "Agregar", 
                        color_scheme="cyan",
                        on_click=AddDocumentState.add_document
                    ),
                    href="/documentos",
                ),
                
                rx.button(
                    "Cancelar",
                    color_scheme="red",
                    #on_click=CountState.decrement,
                ),



                justify="end",
                align="center",
                width="100%"
            ),

            rx.divider(size="4", decorative=True, margin_y="30px"),

            rx.form(
                rx.hstack(
                    rx.vstack(
                        rx.text("Categoría"),
                        # Selector de Categorías
                        rx.select(
                            items=AddDocumentState.all_category_names,
                            placeholder="Selecciona una Categoría",
                            default_value=AddDocumentState.category_name,
                            on_change=AddDocumentState.set_category_name,
                            width="100%",
                        ),
                        width="50%",
                    ),
                    
                    rx.vstack(
                        rx.text("Estante"),
                        # Selector de estantes
                        rx.select(
                            items=AddDocumentState.all_shelve_names,
                            placeholder="Selecciona un Estante",
                            default_value=AddDocumentState.shelve_name,
                            on_change=AddDocumentState.set_shelve_name,
                            width="100%",
                        ),
                        width="50%",
                    ),
                    
                ),
                
                rx.divider(size="4", decorative=True, margin_y="30px"),

                # Componente para subir documentos, recibe un parametro string, que será renderizado como el label
                upload_document("Document"),
                

                #on_submit=AddDocumentState.add_document,
                on_mount=AddDocumentState.load_shelves,
                reset_on_submit=True,
            ),
            
            padding_x="10px",
            padding_y="20px",
            width="100%",
        ),
        
        margin_top="20px",
    )