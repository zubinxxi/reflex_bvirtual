import reflex as rx
from sqlmodel import select

# Modelos
from bvirtual.models.shelves.shelves_models import Shelves

# States
from bvirtual.states.shelves.shelves_state import ShelvesState

class DeleteShelvesState(rx.State):
    """State para eliminar categoría."""
    @rx.event
    def delete_shelves(self, shelve: Shelves):

        try:
            with rx.session() as session:
                shelve_to_delete = session.exec(
                    select(Shelves).where(Shelves.id == shelve.id)).first()
                session.delete(shelve_to_delete)
                session.commit()

                yield ShelvesState.list_shelves()
                yield rx.toast.success(f"Estante \"{shelve.description}\" eliminado con ¡ÉXITO!", duration=5000, position="top-right") 

        except Exception as e:
            yield rx.toast.error(f"Error al eliminar el estante: {str(e)}", duration=5000, position="top-center")  
            print(f"Error al eliminar el estante: {str(e)}")