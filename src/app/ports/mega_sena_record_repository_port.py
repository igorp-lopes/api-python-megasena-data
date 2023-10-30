from typing import Protocol


class MegaSenaRecordRepositoryPort(Protocol):

    async def save_record(self, mega_sena_record):
        ...

    async def save_many_records(self, mega_sena_records):
        ...

    async def get_record_by_id(self, id):
        ...

    async def get_many_records_by_id(self, ids):
        ...

    async def get_record_by_date(self, date):
        ...

    async def get_many_records_by_date_interval(self, start_date, end_date):
        ...
