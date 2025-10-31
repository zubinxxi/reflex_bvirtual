import reflex as rx
from typing import Any
from sqlmodel import select

# Models
from bvirtual.models.auth.auth_models import User_Role

# States
from bvirtual.states.groups.groups_state import GroupsState

class EditGroupState(rx.State):
    name: str
    description: str
    current_group: User_Role = User_Role()

    #Función que trae los datos de un grupo
    @rx.event
    def get_groups(self, group: User_Role):
        self.current_group = group

    @rx.event
    def handle_submit(self, form_data: dict[str, Any]):

        self.name = form_data["name"]
        self.description = form_data["description"]

        try:
            with rx.session() as session:
                """Validaciones"""
                if self.name == "":
                    yield rx.toast.error('El nombre esrequerido', duration="5000", position="top-center")
                    return
                
                if self.description == "":
                    yield rx.toast.error('La descripción es requerida', duration="5000", position="top-center")
                    return

                # 1. Buscamos el grupo a actualizar por su ID
                group = session.exec(
                    select(User_Role).where(User_Role.id == self.current_group.id)
                ).first()

                if not group:
                    yield rx.toast.error(f"Error: No se encontró el grupo con ID {self.current_group.id}.", duration=5000, position="top-center")
                    return
                
                # 2. Verificamos si el nuevo nombre ya existe en otro grupo
                is_group_exist = session.exec(
                    select(User_Role).where(
                        User_Role.name == form_data["name"], 
                        User_Role.id != self.current_group.id  # Excluir el grupo actual
                    )
                ).first()

                if is_group_exist:
                    yield rx.toast.error(f'¡El nombre de grupo "{form_data["name"]}" ya existe!', duration="5000", position="top-center")
                    return
                
                # 3. Actualizamos los campos y guardamos los cambios
                group.name = form_data["name"].upper()
                group.description = form_data["description"].capitalize()

                session.add(group)
                session.commit()
                session.refresh(group)                

                yield GroupsState.list_groups()

                yield rx.toast.success(f"Grupo \"{self.name.upper()}\" actualizado con ¡ÉXITO!", duration=5000, position="top-right")

                self.name = ""
                self.description = ""

        except Exception as e:
            print("Error:", str(e))
            yield rx.toast.error(f"Error al guardar el grupo: {str(e)}", duration=5000, position="top-center")
        