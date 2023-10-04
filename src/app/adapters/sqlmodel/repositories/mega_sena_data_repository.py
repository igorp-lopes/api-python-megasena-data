from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncEngine

from src.app.ports.mega_sena_record_repository_port import MegaSenaRecordRepositoryPort


class MegaSenaDataRepository(MegaSenaRecordRepositoryPort):
    def __init__(self, engine: AsyncEngine):
        self.db = async_sessionmaker(engine, expire_on_commit=False)
