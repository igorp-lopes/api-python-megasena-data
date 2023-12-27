import datetime
from typing import Protocol, Iterable

from src.app.entities.mega_sena_data_model import MegaSenaData


class MegaSenaRecordRepositoryPort(Protocol):
    async def save_record(self, mega_sena_record: MegaSenaData):
        ...

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
