import reflex as rx
import reflex_local_auth

from bvirtual.components.index.document_section import document_section
from bvirtual.template_web import template_web

# State
from bvirtual.states.state import MyLocalAuthState
from bvirtual.states.state import MenuItemsStates
from bvirtual.states.state import IndexState

# Components
from bvirtual.components.index.navbar import navbar_buttons
from bvirtual.components.index.hero import hero
from bvirtual.components.index.menu_category import menu_category
from bvirtual.components.index.footer import footer



@rx.page(
    route="/", 
    title="Inicio | Biblioteca Virtual",
    on_load=IndexState.load_shelves,
)
@template_web
def index() -> rx.Component:
    return rx.box(
        hero(),
        document_section(),
        footer(),
        
    )