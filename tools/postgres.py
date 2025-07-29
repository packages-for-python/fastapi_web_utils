from urllib.parse import quote

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


def create_session(user, password, host, port, database, pool_size=50, max_overflow=0) -> sessionmaker:
    """
    :param pool_size: 连接池大小
    :param max_overflow: 允许超出连接池的连接数
    """
    engine = create_engine("postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(
        quote(user), quote(password), host, port, quote(database)),
        echo=False,
        future=True,
        pool_size=pool_size,
        max_overflow=max_overflow,
        connect_args={"options": "-c timezone=utc"}
    )
    return sessionmaker(bind=engine)


class PostgresClient:
    """通用Postgres客户端SDK,提供连接池和常用数据库操作"""

    def __init__(self, user, password, host, port, database):
        """初始化PostgresClient"""
        self.__session = scoped_session(create_session(user, password, host, port, database, ))

    def __enter__(self):
        return self.__session()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.remove()

    def close(self):
        self.__session.close()

    def get_session(self):
        return self.__session()
