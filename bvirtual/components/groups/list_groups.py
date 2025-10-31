import reflex as rx

# State
from bvirtual.states.groups.groups_state import GroupsState

# Modelo
from bvirtual.models.auth.auth_models import User_Role

# componentes
from bvirtual.components.pagination.pagination import pagination_controls
from bvirtual.components.groups.btn_add_group import add_group_button
from bvirtual.components.groups.btn_edit_group import edit_group_button
from bvirtual.components.groups.btn_del_group import delete_group_button

def show_groups(index: int, group: User_Role) -> rx.Component:
    
    return rx.table.row(
        rx.table.cell(index + 1, align="center"),
        rx.table.cell(group.name, align="center"),
        rx.table.cell(group.description),
        rx.table.cell(
            rx.hstack(
                # Aquí puedes agregar botones o acciones específicas para cada grupo
                rx.tooltip(
                    edit_group_button(group),
                    content="Editar Grupo",
                    side="bottom",
                ),
                rx.tooltip(
                    delete_group_button(group),
                    content="Eliminar Grupo",
                    side="bottom",
                ),
                spacing="2",
                align="center",
                justify="center",
            ),
            align="center",
        ),
    )

def loading_table_groups() -> rx.Component:
    return rx.vstack(
            rx.flex(
                rx.input(
                    placeholder="Buscar grupos...",
                    on_change=lambda value: GroupsState.set_search(value),
                ),
                
                add_group_button(),
                
                direction="row",
                justify="between",
                width="100%",
                margin_top="15px",
            ),

            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("N°", align="center"),
                        rx.table.column_header_cell("Nombre del Grupo", align="center"),
                        rx.table.column_header_cell("Descripción"),
                        rx.table.column_header_cell("Acciones", align="center"),
                    ),
                ),
                rx.table.body(
                    rx.foreach(
                        GroupsState.groups, 
                        lambda group, index: show_groups(index, group)
                    )
                ),
                on_mount=GroupsState.list_groups,
                variant="surface",
                size="1",
                margin_top="20px",
                width="100%",
            ),

            pagination_controls(
                GroupsState.set_limit, 
                GroupsState.prev_page, 
                GroupsState.page_number, 
                GroupsState.total_pages, 
                GroupsState.next_page, 
                GroupsState.total_items
            ),
            
            overflow_y="auto",
        ),



"""rx.vstack(
            rx.hstack(
                rx.spinner(size="3", color="teal"),
                rx.text("Cargando...", font_size="20px", font_weight="bold"),
                spacing="3",
                align="center",
                justify="center",
            ),
            spacing="3",
            align="center",
            justify="center",
        ),"""   

