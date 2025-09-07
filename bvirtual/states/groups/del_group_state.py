import reflex as rx
from sqlmodel import select

# Modelos
from bvirtual.models.auth.auth_models import User_Role

# States
from bvirtual.states.groups.groups_state import GroupsState

class DeleteGroupState(rx.State):
    """State para eliminar grupos."""
    @rx.event
    def delete_group(self, group: User_Role):

        try:
            with rx.session() as session:
                group_to_delete = session.exec(
                    select(User_Role).where(User_Role.id == group.id)).first()
                session.delete(group_to_delete)
                session.commit()

            yield GroupsState.list_groups()
            yield rx.toast.success(f"Usuario \"{group.name}\" eliminado con ¡ÉXITO!", duration=5000, position="top-right") 

        except Exception as e:
            yield rx.toast.error(f"Error al eliminar el grupo: {str(e)}", duration=5000, position="top-center")  
            print(f"Error al eliminar el grupo: {str(e)}")