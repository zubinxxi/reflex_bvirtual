import reflex as rx 

# State
from bvirtual.states.state import MyLocalAuthState
from bvirtual.states.shelves.shelves_state import ShelvesState

#models
from bvirtual.models.shelves.shelves_models import Shelves

# paginado
from bvirtual.components.pagination.pagination import pagination_controls

#from bvirtual.components.categorys.btn_add_category import add_category_button
#from bvirtual.components.categorys.btn_edit_category import edit_category_button
#from bvirtual.components.categorys.btn_del_category import delete_category_button



def show_shelves(index: int, shelve: Shelves) -> rx.Component:
    
    return rx.table.row(
        rx.table.cell(index + 1, align="center"),
        rx.table.cell(shelve.description),
        rx.table.cell(
            rx.hstack(
                rx.tooltip(
                    #edit_shelve_button(shelve),
                    content="Actualizar Usuario",
                    side="bottom",
                ),
                rx.tooltip(
                    #delete_shelve_button(shelve),
                    content="Borrar Usuario",
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


def loading_table_shelves() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.input(
                placeholder="Buscar categoría...",
                on_change=lambda value: ShelvesState.set_search(value),
            ),
            #add_shelve_button(),
            direction="row",
            justify="between",
            width="100%",
            margin_top="15px",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("N°", align="center"),
                    rx.table.column_header_cell("Estante"),
                    rx.table.column_header_cell("Acciones", align="center"),

                ),
            ),
            rx.table.body(
                #rx.foreach(
                #    UserInfoState.users, show_users
                #)
                rx.foreach(
                    ShelvesState.shelves, 
                    lambda user, index: show_shelves(index, user)
                )
            ),
            on_mount=ShelvesState.list_shelves,
            variant="surface",
            size="1",
            margin_top="20px",
            width="100%",
        ),

        pagination_controls(
            ShelvesState.set_limit, 
            ShelvesState.prev_page, 
            ShelvesState.page_number, 
            ShelvesState.total_pages, 
            ShelvesState.next_page, 
            ShelvesState.total_items
        ),
        overflow_y="auto",

    )