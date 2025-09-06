"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from typing import Callable
import reflex as rx
import reflex_local_auth
from rxconfig import config

# Models
from bvirtual.models.auth import auth_models
from bvirtual.models.auth.auth_models import UserInfo

# State
#from biblioteca.state import MyLocalAuthState

# Pages
from bvirtual.pages.index import index
from bvirtual.pages.login_page import login
from bvirtual.pages.users_page import users    

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
