import reflex as rx 

# Importa los dos estados
from bvirtual.states.users.users_state import UserInfoState
from bvirtual.states.users.edit_user_state import EditUserState
from bvirtual.models.auth.auth_models import UserInfo

def edit_user_button(user: UserInfo) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.tooltip(
                    rx.hstack(
                        rx.icon("pencil", size=18),
                    ),
                    content="Actualizar Usuario",
                ),
                color_scheme="blue",
                variant="surface",
                size="1",
            ),
            
        ),

        rx.dialog.content(
            rx.dialog.title(
                "Actualizar Usuario",
            ),

            rx.dialog.description(
                "Actualize los datos del usuario",
            ),

            rx.form(
                rx.flex(
                    rx.input(
                        name="username",
                        placeholder="Usuario",
                        type="text",
                        default_value=user.localuser.username,
                        read_only=True,
                    ),

                    rx.input(
                        name="name",
                        placeholder="Nombre y Apellido",
                        type="text",
                        required=False,
                        spell_check=True,
                        default_value=user.name,
                        auto_focus=True,
                    ),

                    rx.input(
                        name="email",
                        placeholder="user@example.com",
                        type="email",
                        required=False,
                        default_value=user.email,
                    ),

                    rx.input(
                        name="phone",
                        placeholder="Teléfono",
                        type="text",
                        required=False,
                        default_value=user.phone,
                    ),

                    rx.hstack(
                        rx.text("Es Admin"),
                        rx.switch(name="is_admin", default_checked=user.is_admin),
                    ),

                    rx.hstack(
                        rx.text("Activo"),
                        rx.switch(name="enabled", default_checked=user.localuser.enabled),
                    ),

                    # Selector de Rol
                    rx.select(
                        items=EditUserState.all_role_names,
                        placeholder="Selecciona un Rol",
                        default_value=user.user_role.name,
                        on_change=EditUserState.set_role_name,
                        required=True,
                    ),
                
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancelar",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.dialog.close(
                            rx.button(
                                "Guardar",
                                type="submit",
                                variant="soft",
                            ),
                        ),

                        spacing="3",
                        justify="end",
                    ),

                    direction="column",
                    spacing="4",
                    margin_top="15px",
                ),

                on_submit=EditUserState.handle_submit,
                on_mount=EditUserState.load_roles,
                reset_on_submit=True,
            ),
            max_width="450px",
        ),
    )

