import pathlib
import reflex as rx
import reflex_local_auth
from os import remove
from typing import Any, Optional
from bvirtual.models.auth.auth_models import UserInfo

# Clase estado personalizada para manejar la autenticación y obtener información del usuario
class MyLocalAuthState(reflex_local_auth.LocalAuthState):
    @rx.var(cache=True)
    def authenticated_user_info(self) -> Optional[UserInfo]:
        if self.authenticated_user.id < 0:
            return
        with rx.session() as session:
            return session.exec(
                UserInfo.select().where(UserInfo.user_id == self.authenticated_user.id)
            ).one_or_none() 


# Clase estado personalizada para manejar la subida de documentos
class UploadDocumentState(rx.State):
    document_name: str
    uploading: bool = False
    outfile: pathlib.PosixPath = ""

    # Evento que sube el documento a un directorio dentro del proyecto
    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        current_file = files[0] # Archivo que va a subir
        
        upload_data = await current_file.read() # Lectura del archivo que se va a subir
        self.outfile = rx.get_upload_dir() / current_file.filename # Ruta donde se guardará el archivo 

        # Guardar el archivo.
        with self.outfile.open("wb") as file_object:
            file_object.write(upload_data) # Pasamos el archivo leido para ser escrito en la carpeta a guardar

            # Actualizar la variable document_name.
            self.document_name = current_file.filename
            self.uploading = True

    # Evento que cancela la carga del documento y lo borra del directorio uploaded_files
    @rx.event
    def cancel_upload(self):
        self.uploading = False
        if self.outfile:
            remove(self.outfile)
        return rx.cancel_upload("upload1")
    
    @rx.event
    def set_documen_name(self, value: bool):
        if self.document_name:
            self.document_name = value