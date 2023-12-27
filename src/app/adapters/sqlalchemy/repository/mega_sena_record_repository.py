import datetime
from contextlib import AbstractContextManager
from typing import Iterable, Callable

from sqlalchemy.ext.asyncio import AsyncSession

from src.app.adapters.sqlalchemy.entities.mega_sena_record import (
    MegaSenaRecordSQLAlchemy,
)
from src.app.adapters.sqlalchemy.mapper.mega_sena_record_mapper import (
    map_mega_sena_record_to_persistence,
    persistence_to_map_mega_sena_record,
)
from src.app.entities.mega_sena_data_model import MegaSenaData
from src.app.ports.mega_sena_record_repository_port import MegaSenaRecordRepositoryPort


class MegaSenaRecordRepository(MegaSenaRecordRepositoryPort):
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[AsyncSession]]
    ) -> None:
        self.session_factory = session_factory

    async def save_record(self, mega_sena_record: MegaSenaData) -> MegaSenaData:
        record_to_save: MegaSenaRecordSQLAlchemy = map_mega_sena_record_to_persistence(
            mega_sena_record
        )
        async with self.session_factory() as session:
            session.add(record_to_save)
            await session.commit()
            await session.refresh(record_to_save)
            return persistence_to_map_mega_sena_record(record_to_save)

    async def save_many_records(self, mega_sena_records: Iterable[MegaSenaData]):
        ...

    async def get_record_by_id(self, id: int):
        ...

    async def get_many_records_by_id(self, ids: Iterable[int]):
        ...

    async def get_record_by_date(self, date: datetime.date):
        ...

    async def get_many_records_by_date_interval(
        self, start_date: datetime.date, end_date: datetime.date
    ):
        ...
