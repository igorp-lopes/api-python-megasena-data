import os

from dotenv import load_dotenv

load_dotenv()

MEGA_SENA_DATA_URL = "https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx"
MEGA_SENA_DATA_PATH = "src/resources/mega_sena_data.xlsx"
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")

if POSTGRES_USER and POSTGRES_PASSWORD:
    DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:15432/postgres"
else:
    DATABASE_URL = "sqlite+aiosqlite:///./local_db"
