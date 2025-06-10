import reflex as rx
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Construir URL con variables de entorno
db_url = (
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

config = rx.Config(
    app_name="Proyecto_reflex",
    tailwind=None,
    db_url=db_url
)
