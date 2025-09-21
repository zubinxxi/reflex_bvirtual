from os import remove
import pathlib
import reflex as rx
from sqlmodel import select
from typing import Any, Optional

# States
from bvirtual.states.state import UploadDocumentState
#from bvirtual.states.documents.documents_state import DocumentsState

# Models 
from bvirtual.models.documents.document_models import Documents
from bvirtual.models.categorys.categorys_models import Categorys
from bvirtual.models.shelves.shelves_models import Shelves

class AddDocumentState(UploadDocumentState):

    #document_name: str
    #uploading: bool = False
    #outfile: pathlib.PosixPath = ""
    category_name: str # Nombre de la categoría seleccionada
    shelve_name: str # Nombre del estante seleccionado

    all_category_names: list[str] = [] # Lista de nombres de categorías que serán enviadas al frontend
    all_shelve_names: list[str] = [] # Lista de nombres de estentes que serán enviados al frontend

    # Mensajes de estado
    registration_error: str = ""
    success_message: str = ""
    #error_field_name: str = ""
    error_field_category: str = ""
    error_field_shelve: str = ""

    # Metodo para traer las categorías
    def load_categorys(self):
        with rx.session() as session:
            self.all_category_names = session.exec(select(Categorys.description)).all()
            
    def load_shelves(self):
        self.load_categorys()
        with rx.session() as session:
            self.all_shelve_names = session.exec(select(Shelves.description)).all()

    # Eventos que traen el nombre de la categoría y el estante desde los combos (select), y los asignan a las variables de estado
    @rx.event
    def set_category_name(self, category:str):
        self.category_name = category

    @rx.event
    def set_shelve_name(self, shelve: str):
        self.shelve_name = shelve

    # Evento que sube el documento a un directorio dentro del proyecto
    #@rx.event
    #async def handle_upload(self, files: list[rx.UploadFile]):
    #    current_file = files[0] # Archivo que va a subir
    #    upload_data = await current_file.read() # Lectura del archivo que se va a subir
    #    self.outfile = rx.get_upload_dir() / current_file.name # Ruta donde se guardará el archivo 
    #    #self.uploading = True # Activa el check

    #    # Guardar el archivo.
    #    with self.outfile.open("wb") as file_object:
    #        file_object.write(upload_data) # Pasamos el archivo leido para ser escrito en la carpeta a guardar

    #        # Actualizar la variable document_name.
    #        self.document_name = current_file.name
    #        self.uploading = True
        
        

    #@rx.event
    #def cancel_upload(self):
    #    self.uploading = False
    #    if self.outfile:
    #        remove(self.outfile)
    #    return rx.cancel_upload("upload1")


    # Evento que trae los datos del formulario y los guarda en el modelo
    @rx.event
    def add_document(self):

        """Validaciones"""
        #print(form_data)

        if not self.category_name:
            self.error_field_category = "Debe seleccionar una categoría"
            return
        else:
            self.error_field_category = ""

        if not self.shelve_name:
            self.error_field_shelve = "Debe seleccionar un estante"
            return
        else:
            self.error_field_shelve = ""


        try:
            with rx.session() as session:

                # Obtener el ID de la categoría a partir del nombre
                selected_category = session.exec(
                    select(Categorys).where(Categorys.description == self.category_name)
                ).first()

                # Obtener el ID del estante a partir del nombre
                selected_shelve = session.exec(
                    select(Shelves).where(Shelves.description == self.shelve_name)
                ).first()

                session.add(
                    Documents(
                        name=self.document_name,
                        id_categorys=selected_category.id,
                        id_shelves=selected_shelve.id,
                    )
                )
                session.commit()

                self.document_name = ""
                self.uploading = False
                #yield DocumentsState.list_documents()
                yield rx.toast.success(f"Documento \"{UploadDocumentState.document_name}\" creado con ¡ÉXITO!", duration=5000, position="top-right")

            
            


                

        except Exception as e:
            self.registration_error = str(e)
            print(self.registration_error)
            return rx.toast.error(self.registration_error, duration=5000, position="top-rigth")
        
        