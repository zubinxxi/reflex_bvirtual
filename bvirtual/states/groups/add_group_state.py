import reflex as rx
from typing import Any

from sqlmodel import select

# Models
from bvirtual.models.auth.auth_models import User_Role

# States
from bvirtual.states.groups.groups_state import GroupsState

class AddGroupState(rx.State):
    name: str
    description: str

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

                group = session.exec(select(User_Role).where(User_Role.name == self.name)).first()

                if group:
                    yield rx.toast.error('¡El nombre de grupo ya existe!', duration="5000", position="top-center")
                    return

                # Insertar en User_Role
                session.add(
                    User_Role(
                        name = self.name.upper(),
                        description = self.description.capitalize(),
                    )
                )
                session.commit()
                yield GroupsState.list_groups()
                yield rx.toast.success(f"Grupo \"{self.name.upper()}\" creado con ¡ÉXITO!", duration=5000, position="top-right")

                self.name = ""
                self.description = ""

        except Exception as e:
            print("Error:", str(e))
            yield rx.toast.error(f"Error al crear el grupo: {str(e)}", duration=5000, position="top-center")
