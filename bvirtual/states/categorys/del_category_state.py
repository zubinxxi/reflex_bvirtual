import reflex as rx
from sqlmodel import select

# Modelos
from bvirtual.models.categorys.categorys_models import Categorys

# States
from bvirtual.states.categorys.categorys_state import CategorysState

class DeleteCategorysState(rx.State):
    """State para eliminar categoría."""
    @rx.event
    def delete_categorys(self, category: Categorys):

        try:
            with rx.session() as session:
                category_to_delete = session.exec(
                    select(Categorys).where(Categorys.id == category.id)).first()
                session.delete(category_to_delete)
                session.commit()

                yield CategorysState.list_categorys()
                yield rx.toast.success(f"Categoría \"{category.description}\" eliminada con ¡ÉXITO!", duration=5000, position="top-right") 

        except Exception as e:
            yield rx.toast.error(f"Error al eliminar la categoría: {str(e)}", duration=5000, position="top-center")  
            print(f"Error al eliminar la categoría: {str(e)}")