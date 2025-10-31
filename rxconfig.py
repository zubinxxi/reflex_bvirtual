import os
import reflex as rx
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
DB_CONFIG = os.getenv("DB_CONFIG")

config = rx.Config(
    app_name="bvirtual",
    db_url=DB_CONFIG,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)