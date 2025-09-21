"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from typing import Callable
import reflex as rx
import reflex_local_auth
from rxconfig import config

# Models
from bvirtual.models.auth import auth_models
from bvirtual.models.auth.auth_models import UserInfo
from bvirtual.models.categorys.categorys_models import Categorys
from bvirtual.models.shelves.shelves_models import Shelves
from bvirtual.models.documents.document_models import Documents

# State
#from biblioteca.state import MyLocalAuthState

# Pages
from bvirtual.pages.index import index
from bvirtual.pages.login_page import login
from bvirtual.pages.forgot_password_page import forgot_password
from bvirtual.pages.users_page import users    
from bvirtual.pages.groups_page import grupos   
from bvirtual.pages.change_password_page import change_password 
from bvirtual.pages.categorys_page import categorys
from bvirtual.pages.shelves_page import shelves
from bvirtual.pages.documents_page import documents
from bvirtual.pages.add_document_page import add_document

class State(rx.State):
    """The app state."""


        

app = rx.App(
    theme=rx.theme( 
        has_background=True, 
        radius="small", 
        accent_color="cyan",
    ),
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
        "https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200..1000;1,200..1000&family=Raleway:ital,wght@0,100..900;1,100..900&family=Staatliches&display=swap",
    ],
)
