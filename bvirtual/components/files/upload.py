import reflex as rx 

# States
from bvirtual.states.state import UploadDocumentState


def upload_document(label: str) -> rx.Component:
    return rx.vstack(
        rx.text(label),
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
        rx.hstack(
            rx.button(
                "Cargar",
                on_click=UploadDocumentState.handle_upload(
                    rx.upload_files(upload_id="upload1"),
                ),
            ),
            rx.cond(
                UploadDocumentState.uploading,
                rx.button(
                    "Limpiar",
                    on_click=UploadDocumentState.cancel_upload,
                ),
            ),
            
            rx.cond(
                UploadDocumentState.uploading,
                rx.hstack(
                    rx.text(rx.selected_files("upload1")),
                    rx.icon("circle-check", color="green")
                ),
                rx.text(rx.selected_files("upload1")),
            ),

            justify="start",
            align="center",
            width="100%"
        ),
        width="100%",
        justify="center",
        align="start",
    ),