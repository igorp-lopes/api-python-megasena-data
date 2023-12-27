from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class MegaSenaData(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    concurso: int
    data_do_sorteio: date
    bola1: int
    bola2: int
    bola3: int
    bola4: int
    bola5: int
    bola6: int
    ganhadores_6_acertos: int
    cidade_uf: Optional[str] = None
    rateio_6_acertos: str
    ganhadores_5_acertos: int
    rateio_5_acertos: str
    ganhadores_4_acertos: int
    rateio_4_acertos: str
    acumulado_6_acertos: str
    arrecadacao_total: str
    estimativa_premio: str
    acumulado_sorteio_especial_mega_da_virada: str
    observacao: Optional[str] = None
