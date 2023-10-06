from typing import Iterable

from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from src.app.adapters.sqlmodel.entities.mega_sena_data import SqlModelMegaSenaData
from src.app.ports.mega_sena_record_repository_port import MegaSenaRecordRepositoryPort


class MegaSenaDataRepository(MegaSenaRecordRepositoryPort):
    def __init__(self, engine: AsyncEngine):
        self.session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


    async def save_record(self, mega_sena_record: SqlModelMegaSenaData):
        async with self.session() as session:
            session.add(mega_sena_record)
            await session.commit()
            await session.refresh(mega_sena_record)
            return mega_sena_record

    async def save_many_records(self, mega_sena_records: Iterable[SqlModelMegaSenaData]):
        async with self.session() as session:
            session.add_all(mega_sena_records)
            await session.commit()
            await session.refresh(mega_sena_records)
            return mega_sena_records
