from abc import ABC, abstractmethod


class MegaSenaRecordRepositoryPort(ABC):

    @abstractmethod
    def save_record(self, mega_sena_record):
        ...

    def save_many_records(self, mega_sena_records):
        ...

    def get_record_by_id(self, mega_sena_id):
        ...

    def get_many_records_by_id(self, mega_sena_ids):
        ...

    def update_record(self, mega_sena_record):
        ...

    def update_many_records(self, mega_sena_records):
        ...

    def get_record_by_date(self):
        ...

    def get_many_records_by_date_interval(self, date_interval):
        ...
