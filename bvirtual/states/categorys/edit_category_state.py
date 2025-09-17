import reflex as rx
from typing import Any
from sqlmodel import select

# Models
from bvirtual.models.categorys.categorys_models import Categorys

# States
from bvirtual.states.categorys.categorys_state import CategorysState

class EditCategoryState(rx.State):
    description: str
    current_category: Categorys = Categorys()

    #Función que trae los datos de una categoría desde el grid
    @rx.event
    def get_category(self, category: Categorys):
        self.current_category = category

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
                category = session.exec(
                    select(Categorys).where(Categorys.id == self.current_category.id)
                ).first()

                if not category:
                    yield rx.toast.error(f"Error: No se encontró la categoría con ID {self.current_category.id}.", duration=5000, position="top-center")
                    return
                
                # 2. Verificamos si la nueva categoría ya existe
                is_category_exist = session.exec(
                    select(Categorys).where(Categorys.description == form_data["description"]).where(Categorys.id != self.current_category.id)  # Excluir la categoría actual
                ).first()

                if is_category_exist:
                    yield rx.toast.error(f"¡El nombre de la categoría \"{form_data["name"]}\" ya existe!", duration="5000", position="top-center")
                    return
                
                # 3. Actualizamos los campos y guardamos los cambios
                category.description = form_data["description"].title()

                session.add(category)
                session.commit()
                session.refresh(category)                

            yield CategorysState.list_categorys()

            yield rx.toast.success(f"Categoría \"{self.description.title()}\" actualizada con ¡ÉXITO!", duration=5000, position="top-right")

            self.description = ""

        except Exception as e:
            print("Error:", str(e))
            yield rx.toast.error(f"Error al guardar la categoría: {str(e)}", duration=5000, position="top-center")
        