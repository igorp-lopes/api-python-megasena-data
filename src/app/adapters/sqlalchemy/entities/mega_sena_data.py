from sqlalchemy import Integer, String, Column, Date
from sqlalchemy.orm import DeclarativeBase


class MegaSenaData(DeclarativeBase):
    __tablename__ = 'mega_sena_data'

    concurso = Column(Integer, primary_key=True)
    data_do_sorteio = Column(Date)
    bola1 = Column(Integer)
    bola2 = Column(Integer)
    bola3 = Column(Integer)
    bola4 = Column(Integer)
    bola5 = Column(Integer)
    bola6 = Column(Integer)
    ganhadores_6_acertos = Column(Integer)
    cidade_UF = Column(String)
    rateio_6_acertos = Column(String)
    ganhadores_5_acertos = Column(Integer)
    rateio_5_acertos = Column(String)
    ganhadores_4_acertos = Column(Integer)
    rateio_4_acertos = Column(String)
    acumulado_6_acertos = Column(String)
    arrecadacao_total = Column(String)
    estimativa_premio = Column(String)
    acumulado_sorteio_especial_mega_da_virada = Column(String)
    observacao = Column(String)
