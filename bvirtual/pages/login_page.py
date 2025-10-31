import reflex as rx
import reflex_local_auth

from bvirtual.template_auth import template_auth
from bvirtual.components.auth.form_login import form_login

@rx.page(
    route="/login",
    title="Login | Biblioteca Virtual",
)
@template_auth
def login() -> rx.Component:
    return form_login()