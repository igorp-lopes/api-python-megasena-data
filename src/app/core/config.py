import os

MEGA_SENA_DATA_URL = "https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx"

MEGA_SENA_DATA_PATH = "src/resources/mega_sena_data.xlsx"

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite+aiosqlite:///./local_db")
