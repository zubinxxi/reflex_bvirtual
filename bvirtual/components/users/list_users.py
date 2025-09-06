import reflex as rx 

# State
from bvirtual.states.state import MyLocalAuthState
from bvirtual.states.users.users_state import UserInfoState
from bvirtual.models.auth.auth_models import UserInfo

from bvirtual.components.users.btn_add_user import add_user_button
from bvirtual.components.users.btn_edit_user import edit_user_button
from bvirtual.components.users.btn_del_user import delete_user_button



def show_users(index: int, user: UserInfo) -> rx.Component:
    
    return rx.table.row(
        rx.table.cell(index + 1, align="center"),
        rx.table.cell(user.localuser.username, align="center"),
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.phone, align="center"),
        rx.table.cell(user.user_role.name),
        rx.table.cell(
            rx.cond(
                user.localuser.enabled,
                #rx.badge(rx.icon('circle-check'),color_scheme="green"),
                rx.icon('circle-check', color="cyan"),
                #rx.badge(rx.icon('circle-x'), color_scheme="red"),
                rx.icon('circle-x', color="tomato"),
            ),
            align="center",
        ),
        rx.table.cell(
            rx.cond(
                user.is_admin,
                rx.icon('circle-check', color="cyan"),
                rx.icon('circle-x', color="tomato"),
            ),
            align="center",
        ),
        rx.table.cell(
            rx.hstack(
                rx.tooltip(
                    edit_user_button(user),
                    content="Actualizar Usuario",
                    side="bottom",
                ),
                rx.tooltip(
                    delete_user_button(user),
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


def loading_table_users() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.input(
                placeholder="Buscar usuarios...",
                on_change=lambda value: UserInfoState.set_search(value),
            ),
            add_user_button(),
            direction="row",
            justify="between",
            width="100%",
            margin_top="15px",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("N°", align="center"),
                    rx.table.column_header_cell("Usuario", align="center"),
                    rx.table.column_header_cell("Nombre y Apellido"),
                    rx.table.column_header_cell("Correo"),
                    rx.table.column_header_cell("Teléfono", align="center"),
                    rx.table.column_header_cell("Rol"),
                    rx.table.column_header_cell("Activo", align="center"),
                    rx.table.column_header_cell("Es Admin", align="center"),
                    rx.table.column_header_cell("Acciones", align="center"),

                ),
            ),
            rx.table.body(
                #rx.foreach(
                #    UserInfoState.users, show_users
                #)
                rx.foreach(
                    UserInfoState.users, 
                    lambda user, index: show_users(index, user)
                )
            ),
            on_mount=UserInfoState.list_users,
            variant="surface",
            size="1",
            margin_top="20px",
            width="100%",
        ),

        rx.hstack(
            rx.hstack(
                rx.text("Ver"),
                rx.select(
                    ["5", "10", "25", "50"],
                    default_value = "10",
                    on_change = lambda value: UserInfoState.set_limit(value),
                    size="1",
                    width="70px",
                ),
                rx.text("entradas"),
                width="20%",
                align="center",
                justify="start",
            ),

            rx.hstack(
                rx.button(
                    "Anterior",
                    on_click=UserInfoState.prev_page,
                    variant="surface",
                    size="1",
                ),
                rx.text(
                    f"Page {UserInfoState.page_number} / {UserInfoState.total_pages}"
                ),
                rx.button(
                    "Siguiente",
                    on_click=UserInfoState.next_page,
                    variant="surface",
                    size="1",
                ),
                width="60%",
                align="center",
                justify="center",
            ),
            
            rx.hstack(
                rx.text(f"Total de usuarios: {UserInfoState.total_items}"),
                width="20%",
                align="center",
                justify="end",
            ),

            width="100%",
            align="center",
            justify="between",
        ),
        overflow_y="auto",

    )