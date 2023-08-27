from typing import Protocol


class MegaSenaRepository(Protocol):

    def save(self, mega_sena_record):
        ...

    def save_many(self, mega_sena_records):
        ...

    def update(self, mega_sena_record):
        ...

    def update_many(self, mega_sena_records):
        ...

    def get_by_date(self):
        ...

    def get_many_by_date_interval(self, date_interval):
        ...
