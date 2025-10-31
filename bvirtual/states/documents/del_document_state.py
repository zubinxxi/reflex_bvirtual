import reflex as rx 
import pathlib
from os import remove, listdir
from sqlmodel import select



# Models 
from bvirtual.models.documents.document_models import Documents

# States
from bvirtual.states.documents.documents_state import DocumentsState

class DeleteDocumentState(rx.State):
    """State para eliminar documentos."""

    file: pathlib.PosixPath = ""

    @rx.event
    def delete_document(self, document: Documents):

        try:
            with rx.session() as session:

                document_to_delete = session.exec(
                    select(Documents).where(Documents.id == document.id)).first()
                session.delete(document_to_delete)
                session.commit()

                if document_to_delete.name in listdir(rx.get_upload_dir()):
                    self.file = rx.get_upload_dir() / document_to_delete.name # Ruta donde se guardó el archivo 
                    remove(self.file)

                yield DocumentsState.list_documents()
                yield rx.toast.success(f"Documento: {document.name}, eliminado con ¡ÉXITO!", duration=5000, position="top-right") 

        except Exception as e:
            yield rx.toast.error(f"Error al eliminar el documento: {str(e)}", duration=5000, position="top-center")  
            print(f"Error al eliminar el documento: {str(e)}")