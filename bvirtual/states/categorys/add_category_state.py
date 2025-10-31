import reflex as rx
from typing import Any

from sqlmodel import select

# Models
from bvirtual.models.categorys.categorys_models import Categorys

# States
from bvirtual.states.categorys.categorys_state import CategorysState

class AddCategoryState(rx.State):
    description: str 


    @rx.event
    def handle_submit(self, form_data: dict[str, Any]): 

        self.description = form_data["description"] 

        try:            
            with rx.session() as session:

                """Validaciones"""
                if self.description == "":
                    yield rx.toast.error('La descripción es requerida', duration="5000", position="top-center")
                    return

                #buscamos si la categoría existe en la DB.
                category = session.exec(select(Categorys).where(Categorys.description == self.description)).first()

                #Si existe en la DB, no se guarda y emite un mensaje en pantalla.
                if category:
                    yield rx.toast.error('¡El nombre de la categoría ya existe!', duration="5000", position="top-center")
                    return
                
                
                # Insertar en User_Role
                session.add(
                    Categorys(
                        description = self.description.title(),
                    )
                )
                session.commit()
                yield CategorysState.list_categorys()
                yield rx.toast.success(f"Categoría \"{self.description}\" creada con ¡ÉXITO!", duration=5000, position="top-right")

                self.description = ""
            

        except Exception as e:
            print("Error:", str(e))
            yield rx.toast.error(f"Error al crear la categoría: {str(e)}", duration=5000, position="top-center")
