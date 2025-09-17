import reflex as rx
from typing import Any

from sqlmodel import select

# Models
from bvirtual.models.shelves.shelves_models import Shelves

# States
from bvirtual.states.shelves.shelves_state import ShelvesState

class AddShelveState(rx.State):
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
                shelve = session.exec(select(Shelves).where(Shelves.description == self.description)).first()

                #Si existe en la DB, no se guarda y emite un mensaje en pantalla.
                if shelve:
                    yield rx.toast.error('¡El nombre del estante ya existe!', duration="5000", position="top-center")
                    return
                
                
                # Insertar en User_Role
                session.add(
                    Shelves(
                        description = self.description.title(),
                    )
                )
                session.commit()
                yield ShelvesState.list_shelves()
                yield rx.toast.success(f"Estante \"{self.description}\" creado con ¡ÉXITO!", duration=5000, position="top-right")

                self.description = ""
            

        except Exception as e:
            print("Error:", str(e))
            yield rx.toast.error(f"Error al crear el estante: {str(e)}", duration=5000, position="top-center")
