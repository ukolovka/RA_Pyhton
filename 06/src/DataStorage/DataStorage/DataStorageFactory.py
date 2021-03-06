from DataStorage import *


class DataStorageFactory(object):
    __storages = {
        'memory': MemoryDataStorage,
        'mongo': MongoDataStorage,
        'postgres': PostgresDataStorage,
        'sqlite': SqliteDataStorage,
    }

    @classmethod
    async def create_storage(cls, settings: dict) -> DataStorage:
        storage: DataStorage = cls.__storages[settings.get('storage', 'memory')]()

        if isinstance(storage, MongoDataStorage):
            await storage.create(settings['database'], settings['collection'])
        elif isinstance(storage, PostgresDataStorage):
            await storage.create(settings['connection'])
        elif isinstance(storage, SqliteDataStorage):
            await storage.create(settings['filename'])

        return storage
