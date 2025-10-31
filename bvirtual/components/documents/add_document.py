import reflex as rx 

# States
#from bvirtual.states.state import UploadDocumentState
from bvirtual.states.documents.add_document_state import AddDocumentState

# Components
#from bvirtual.components.files.upload import upload_document

color = "rgb(107,99,246)"

def upload_document(label: str) -> rx.Component:
    return rx.vstack(
        rx.text(label),
        rx.hstack(
            rx.button(
                "Cargar",
                on_click=AddDocumentState.handle_upload(
                    rx.upload_files(upload_id="upload1"),
                ),
            ),
            rx.cond(
                AddDocumentState.uploading,
                rx.button(
                    "Limpiar",
                    on_click=AddDocumentState.cancel_upload,
                ),
            ),
            
            rx.cond(
                AddDocumentState.uploading,
                rx.hstack(
                    rx.text(rx.selected_files("upload1")),
                    rx.icon("circle-check", color="green"),
                    justify="between",
                    align="center",
                ),
                rx.text(rx.selected_files("upload1")),
            ),

            justify="start",
            align="center",
            width="100%"
        ),
        rx.upload(
            rx.vstack(
                rx.button(
                    "Seleccione el archivo",
                    color="#424242",
                    bg="white",
                    border=f"1px solid {rx.color('cyan')}",
                ),
                rx.text(
                    "Arrastre y suelte archivos aquí o haga clic para seleccionar archivos"
                ),
            ),
            id="upload1",
            accept={
                "application/pdf": [".pdf"],
                #"image/png": [".png"],
                #"image/jpeg": [".jpg", ".jpeg"],
                #"image/gif": [".gif"],
                #"image/webp": [".webp"],
                #"text/html": [".html", ".htm"],
            },
            max_files=1,
            border=f"1px dotted {rx.color('cyan')}",
            padding="5em",
            width="100%",
        ),
        rx.cond(
            AddDocumentState.error_field_filename,
            rx.text(
                rx.hstack(
                    rx.icon("circle-x", color="tomato"),
                    AddDocumentState.error_field_filename,
                    justify="between",
                    align="center",
                ), 
                color="tomato",
            ),
        ),
        
        width="100%",
        justify="center",
        align="start",
        on_mount=rx.clear_selected_files("upload1")
    ),

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
                    #href="/documentos",
                ),
                
                rx.link(
                    rx.button(
                        "Calcelar", 
                        color_scheme="tomato",
                        on_click=AddDocumentState.cancel_upload
                    ),
                    href="/documentos",
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
                        rx.cond(
                            AddDocumentState.error_field_category,
                            rx.text(
                                rx.hstack(
                                    rx.icon("circle-x", color="tomato"),
                                    AddDocumentState.error_field_category,
                                    justify="between",
                                    align="center",
                                ),
                                color="tomato",
                            )                        
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
                        rx.cond(
                            AddDocumentState.error_field_shelve,
                            rx.text(
                                rx.hstack(
                                    rx.icon("circle-x", color="tomato"),
                                    AddDocumentState.error_field_shelve,
                                    justify="between",
                                    align="center",
                                ), 
                                color="tomato",
                            ),                        
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