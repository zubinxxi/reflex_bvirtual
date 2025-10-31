import reflex as rx
import reflex_local_auth

from bvirtual.template_auth import template_auth
from bvirtual.components.auth.form_forgot_password import form_forgot_password

@rx.page(
    route="/forgot-password",
    title="Recuperar Contraseña | Biblioteca Virtual",
)
@template_auth
def forgot_password() -> rx.Component:
    return form_forgot_password()