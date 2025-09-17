import reflex as rx
from typing import Any
from sqlmodel import select

# Models
from bvirtual.models.shelves.shelves_models import Shelves

# States
from bvirtual.states.shelves.shelves_state import ShelvesState

class EditShelveState(rx.State):
    description: str
    current_shelve: Shelves = Shelves()

    #Función que trae los datos de un estante
    @rx.event
    def get_shelve(self, shelve: Shelves):
        self.current_shelve = shelve

    @rx.event
    def handle_submit(self, form_data: dict[str, Any]):

        self.description = form_data["description"]

        try:
            with rx.session() as session:

                """Validaciones"""                
                if self.description == "":
                    yield rx.toast.error('La descripción es requerida', duration="5000", position="top-center")
                    return

                # 1. Buscamos la categoría a actualizar por su ID
                shelve = session.exec(
                    select(Shelves).where(Shelves.id == self.current_shelve.id)
                ).first()

                if not shelve:
                    yield rx.toast.error(f"Error: No se encontró el estante con ID {self.current_shelve.id}.", duration=5000, position="top-center")
                    return
                
                # 2. Verificamos si la nueva categoría ya existe
                is_shelve_exist = session.exec(
                    select(Shelves).where(
                        Shelves.description == form_data["description"], 
                        Shelves.id != self.current_shelve.id  # Excluir el estante actual
                    )
                ).first()

                if is_shelve_exist:
                    yield rx.toast.error(f'¡El nombre del estante "{form_data["name"]}" ya existe!', duration="5000", position="top-center")
                    return
                
                # 3. Actualizamos los campos y guardamos los cambios
                shelve.description = form_data["description"].title()

                session.add(shelve)
                session.commit()
                session.refresh(shelve)                

            yield ShelvesState.list_shelves()
            yield rx.toast.success(f"Estante \"{self.description.title()}\" actualizado con ¡ÉXITO!", duration=5000, position="top-right")

            self.description = ""

        except Exception as e:
            print("Error:", str(e))
            yield rx.toast.error(f"Error al guardar el estante: {str(e)}", duration=5000, position="top-center")
        