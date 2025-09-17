import reflex as rx
from typing import Optional, List
from sqlmodel import Field, Relationship 

# No importa Categorys y Shelves aquí
#from bvirtual.models.categorys.categorys_models import Categorys
#from bvirtual.models.shelves.shelves_models import Shelves

class Documents(rx.Model, table=True):
    name: str = Field(nullable=True)
    id_shelves: int = Field(nullable=True, foreign_key="shelves.id", ondelete="SET NULL")
    id_categorys: int = Field(nullable=True, foreign_key="categorys.id", ondelete="SET NULL")

    categorys: Optional["Categorys"] = Relationship(back_populates="documents")  # type: ignore # Relationship to the LocalUser model
    shelves: Optional["Shelves"] = Relationship(back_populates="documents")  # type: ignore # Relationship to the User_Role model