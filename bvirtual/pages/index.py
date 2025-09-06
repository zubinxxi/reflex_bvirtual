import reflex as rx
import reflex_local_auth

from bvirtual.template import template

# State
from bvirtual.states.state import MyLocalAuthState

@rx.page(route="/", title="Dashboard | Biblioteca Virtual")
@template
@reflex_local_auth.require_login
def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Dashboard", 
                size="5", 
                font_family="Staatliches",
                letter_spacing="2px",
            ),
            width="100%",
        ),
        rx.container(
            #rx.color_mode.button(position="top-right"),
            rx.vstack(
                rx.cond(
                    MyLocalAuthState.authenticated_user_info,
                    # Componente para el caso 'verdadero'
                    rx.fragment(
                        rx.heading(f"Bienvenid@, {MyLocalAuthState.authenticated_user_info.name}", size="9"),
                        rx.hstack(
                            rx.text('Correo verificado:', size="7", font_weight="bold", color="cyan"),
                            rx.text(f"{MyLocalAuthState.authenticated_user_info.email}", size="7"),
                        ),
                    ),
                    
                    # Componente para el caso 'falso'
                    rx.heading("Bienvenido a Biblioteca Virtual", size="9"),
                ),
                
                rx.link(
                    rx.button("Logout"),
                    href="/login",
                    is_external=False,
                    on_click=reflex_local_auth.LocalAuthState.do_logout,
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
            ),
        ),
        padding_y="20px",
        
    )