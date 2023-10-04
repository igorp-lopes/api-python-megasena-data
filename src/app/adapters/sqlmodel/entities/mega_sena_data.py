from datetime import datetime
from typing import Optional
from sqlmodel import Field

from src.app.adapters.sqlmodel.entities.base_entity import SqlModelBaseEntity


class SqlModelMegaSenaData(SqlModelBaseEntity, table=True):

    concurso: int = Field(default=None, primary_key=True)
    data_do_sorteio: datetime
    bola1: int
    bola2: int
    bola3: int
    bola4: int
    bola5: int
    bola6: int
    ganhadores_6_acertos: int
    cidade_UF: str
    rateio_6_acertos: str
    ganhadores_5_acertos: int
    rateio_5_acertos: str
    ganhadores_4_acertos: int
    rateio_4_acertos: str
    acumulado_6_acertos: str
    arrecadacao_total: str
    estimativa_premio: str
    acumulado_sorteio_especial_mega_da_virada: str
    observacao: Optional[str]
