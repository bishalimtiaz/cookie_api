# dialect+driver://username:password@host:port/database
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = 'mysql+mysqldb://root:root@127.0.0.1:3306/cookie_db'

'''
The `echo` flag is a shortcut to setting up SQLAlchemy logging, 
which is accomplished via Python’s standard logging module'''
'''
The return value of create_engine() is an instance of Engine, 
and it represents the core interface to the database, adapted 
through a dialect that handles the details of the database and DBAPI in use. 
In this case the SQLite dialect will interpret instructions to the Python built-in sqlite3 module
'''

''' `pool_pre_ping` boolean, if True will enable the connection pool “pre-ping” feature 
that tests connections for liveness upon each checkout. '''
'''
The new base class will be given a metaclass that produces
    appropriate :class:`~sqlalchemy.schema.Table` objects and makes
    the appropriate :func:`~sqlalchemy.orm.mapper` calls based on the
    information provided declaratively in the class and any subclasses
    of the class.'''

Base = declarative_base()

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession,
)


async def init_models():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
