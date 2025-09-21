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
#from bvirtual.components.categorys.btn_del_category import delete_category_button



def show_documents(index: int, documents: Documents) -> rx.Component:
    
    return rx.table.row(
        rx.table.cell(index + 1, align="center"),
        rx.table.cell(documents.categorys.description),
        rx.table.cell(documents.shelves.description),
        rx.table.cell(documents.name),
        rx.table.cell(
            rx.hstack(
                rx.tooltip(
                    #edit_category_button(documents),
                    content="Actualizar Documento",
                    side="bottom",
                ),
                rx.tooltip(
                    #delete_documento_button(documents),
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