import reflex as rx 

# State
from bvirtual.states.state import MyLocalAuthState
from bvirtual.states.documents.documents_state import DocumentsState

#models
from bvirtual.models.documents.document_models import Documents


# paginado
from bvirtual.components.pagination.pagination import pagination_controls

#from bvirtual.components.categorys.btn_add_category import add_category_button
#from bvirtual.components.categorys.btn_edit_category import edit_category_button
from bvirtual.components.documents.btn_del_document import delete_document_button


def view_pdf(pdf:str) -> rx.Component:

    pass


def show_documents(index: int, documents: Documents) -> rx.Component:
    
    return rx.table.row(
        rx.table.cell(index + 1, align="center"),
        rx.table.cell(documents.categorys.description),
        rx.table.cell(documents.shelves.description),
        rx.table.cell(documents.name),
        rx.table.cell(
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.button(
                        rx.tooltip(
                            rx.icon(
                                "file-text",
                                size=20,
                                color="tomato",
                            ),
                            content="Ver PDF",
                        ),
                        color_scheme="tomato",
                        variant="ghost",
                    ),
                ),

                rx.dialog.content(
                    rx.dialog.title(
                        documents.name,
                        #rx.get_upload_url(documents.name)
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
            align="center"
        ),
        rx.table.cell(
            rx.hstack(
                rx.tooltip(
                    #edit_category_button(documents),
                    content="Actualizar Documento",
                    side="bottom",
                ),
                rx.tooltip(
                    delete_document_button(documents),
                    content="Borrar Documento",
                    side="bottom",
                ),
                
                
                spacing="2",
                align="center",
                justify="center",
            ),
            
            
        ),
        align="center",
        style={"_hover": {"bg": rx.color("gray", 3)}},
    )


def loading_table_documents() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.input(
                placeholder="Buscar Documento...",
                on_change=lambda value: DocumentsState.set_search(value),
            ),
            #add_document_button(),
            rx.button(
                rx.tooltip(
                    rx.hstack(
                        rx.icon("plus", size=18),
                        rx.text("Nuevo", size="4"),
                        align="center",
                        justify="center",
                    ),
                    content="Agregar Documento",
                ),
                color_scheme="cyan",
                variant="surface",
                on_click=rx.redirect('/agregar-documento')
            ),
            direction="row",
            justify="between",
            width="100%",
            margin_top="15px",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("N°", align="center"),
                    rx.table.column_header_cell("Categoría"),
                    rx.table.column_header_cell("Estante"),
                    rx.table.column_header_cell("Documento"),
                    rx.table.column_header_cell("Ver", align="center"),
                    rx.table.column_header_cell("Acciones", align="center"),

                ),
            ),
            rx.table.body(
                #rx.foreach(
                #    UserInfoState.users, show_users
                #)
                rx.foreach(
                    DocumentsState.documents, 
                    lambda documents, index: show_documents(index, documents)
                )
            ),
            on_mount=DocumentsState.list_documents,
            variant="surface",
            size="1",
            margin_top="20px",
            width="100%",
        ),

        pagination_controls(
            DocumentsState.set_limit, 
            DocumentsState.prev_page, 
            DocumentsState.page_number, 
            DocumentsState.total_pages, 
            DocumentsState.next_page, 
            DocumentsState.total_items
        ),
        overflow_y="auto",

    )