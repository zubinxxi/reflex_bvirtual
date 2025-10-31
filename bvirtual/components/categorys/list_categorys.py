import reflex as rx 

# State
from bvirtual.states.state import MyLocalAuthState
from bvirtual.states.categorys.categorys_state import CategorysState

#models
from bvirtual.models.categorys.categorys_models import Categorys

# paginado
from bvirtual.components.pagination.pagination import pagination_controls

from bvirtual.components.categorys.btn_add_category import add_category_button
from bvirtual.components.categorys.btn_edit_category import edit_category_button
from bvirtual.components.categorys.btn_del_category import delete_category_button



def show_categorys(index: int, category: Categorys) -> rx.Component:
    
    return rx.table.row(
        rx.table.cell(index + 1, align="center"),
        rx.table.cell(category.description),
        rx.table.cell(
            rx.hstack(
                rx.tooltip(
                    edit_category_button(category),
                    content="Actualizar Usuario",
                    side="bottom",
                ),
                rx.tooltip(
                    delete_category_button(category),
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


def loading_table_categorys() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.input(
                placeholder="Buscar categoría...",
                on_change=lambda value: CategorysState.set_search(value),
            ),
            add_category_button(),
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
                    rx.table.column_header_cell("Acciones", align="center"),

                ),
            ),
            rx.table.body(
                #rx.foreach(
                #    UserInfoState.users, show_users
                #)
                rx.foreach(
                    CategorysState.categorys, 
                    lambda user, index: show_categorys(index, user)
                )
            ),
            on_mount=CategorysState.list_categorys,
            variant="surface",
            size="1",
            margin_top="20px",
            width="100%",
        ),

        pagination_controls(
            CategorysState.set_limit, 
            CategorysState.prev_page, 
            CategorysState.page_number, 
            CategorysState.total_pages, 
            CategorysState.next_page, 
            CategorysState.total_items
        ),
        overflow_y="auto",

    )