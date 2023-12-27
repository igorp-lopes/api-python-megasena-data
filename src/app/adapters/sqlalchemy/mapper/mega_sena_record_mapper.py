from src.app.adapters.sqlalchemy.entities.mega_sena_record import (
    MegaSenaRecordSQLAlchemy,
)
from src.app.entities.mega_sena_data_model import MegaSenaData


def map_mega_sena_record_to_persistence(
    record: MegaSenaData, **extra_attributes
) -> MegaSenaRecordSQLAlchemy:
    record_dict = record.model_dump()
    if extra_attributes:
        return MegaSenaRecordSQLAlchemy(**record_dict)
    else:
        return MegaSenaRecordSQLAlchemy(**record_dict)


def persistence_to_map_mega_sena_record(
    record: MegaSenaRecordSQLAlchemy,
) -> MegaSenaData:
    return MegaSenaData.model_validate(record)
