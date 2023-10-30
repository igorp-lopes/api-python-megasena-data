from typing import Iterable

from src.app.entities.mega_sena_data_model import MegaSenaData
from src.app.ports.mega_sena_record_repository_port import MegaSenaRecordRepositoryPort


class MegaSenaDataService:
    def __init__(self, mega_sena_data_repository: MegaSenaRecordRepositoryPort):
        self.mega_sena_data_repository = mega_sena_data_repository

    async def _save_mega_sena_record(self, mega_sena_record: MegaSenaData):
        return self.mega_sena_data_repository.save_record(mega_sena_record)

    async def _save_many_mega_sena_records(
        self, mega_sena_records: Iterable[MegaSenaData]
    ):
        return self.mega_sena_data_repository.save_many_records(mega_sena_records)
