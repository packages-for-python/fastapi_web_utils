from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class ClickhouseClient:

    def __init__(self, user, password, host, port, database):
        engine = create_engine(
            f'clickhouse+native://{user}:{quote_plus(password)}@{host}:{port}/{database}',
            pool_size=10,
            max_overflow=20,
            pool_timeout=30,
            pool_recycle=3600,
            pool_pre_ping=True,
            connect_args={
                'settings': {
                    'max_block_size': 100000,
                    'socket_timeout': 3600,
                    'connect_timeout': 10,
                }
            },
        )
        self.__session = scoped_session(sessionmaker(bind=engine))

    def __enter__(self):
        return self.__session()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.remove()

    def close(self):
        self.__session.close()

    def get_session(self):
        return self.__session()
