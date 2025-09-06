import re
import reflex as rx 
import reflex_local_auth
from reflex_local_auth.local_auth import LocalAuthState
from bvirtual.states.users.add_user_state import AddUserState


"""Funcion que maneja el formulario para agregar un nuevo usuario"""
def add_user_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.tooltip(
                    rx.hstack(
                        rx.icon("plus", size=18),
                        rx.text("Nuevo", size="4"),
                        align="center",
                        justify="center",
                    ),
                    content="Crear Usuario",
                ),
                color_scheme="cyan",
                variant="surface",
            ),
        ),

        rx.dialog.content(
            rx.dialog.title(
                "Agregar Nuevo Usuario",
            ),

            rx.dialog.description(
                "Agregue usuarios al sistema",
            ),

            rx.form(
                rx.flex(
                    rx.input(
                        name="username",
                        placeholder="Usuario",
                        type="text",
                        default_value=AddUserState.username,
                        required=True,
                        spell_check=True,
                    ),

                    rx.input(
                        name="name",
                        placeholder="Nombre y Apellido",
                        type="text",
                        default_value=AddUserState.name,
                        required=False,
                        text_transform="capitalize",
                    ),

                    rx.input(
                        name="email",
                        placeholder="user@example.com",
                        type="text",
                        default_value=AddUserState.email,
                        required=True,
                    ),

                    rx.input(
                        name="phone",
                        placeholder="Teléfono",
                        type="text",
                        default_value=AddUserState.phone,
                        required=False,
                    ),

                    rx.input(
                        name="password",
                        placeholder="Contraseña",
                        type="password",
                        default_value=AddUserState.password,
                        required=False,
                    ),
                    
                    rx.input(
                        name="confirm_password",
                        placeholder="Repetir contraseña",
                        type="password",
                        default_value=AddUserState.confirm_password,
                        required=False,
                    ),

                    #switch_is_admin(),
                    rx.hstack(
                        rx.text("Es Admin"),
                        rx.switch(name="is_admin", default_checked=False),
                    ),

                    # Selector de Rol
                    rx.select(
                        items=AddUserState.all_role_names,
                        placeholder="Selecciona un Rol",
                        default_value=AddUserState.role_name,
                        on_change=AddUserState.set_role_name,
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

                on_submit=AddUserState.handle_submit,
                on_mount=AddUserState.load_roles,
                reset_on_submit=True,
            ),
            max_width="450px",
        ),
    )