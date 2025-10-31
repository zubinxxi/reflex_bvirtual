import reflex as rx
from typing import Optional, List
from sqlmodel import Field, Relationship 

# No importa Documents aquí
# from bvirtual.models.documents.document_models import Documents

class Categorys(rx.Model, table=True):
    description: str = Field(nullable=True)  # Optional description of the category

    documents: List["Documents"]= Relationship(back_populates="categorys")  # type: ignore # Relationship to Documents model