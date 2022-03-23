# dialect+driver://username:password@host:port/database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import get_settings

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
DB = get_settings().db

engine = create_engine(
    DB,
    echo=True,
    pool_pre_ping=True,
)

Session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


def init_models():
    with engine.begin() as conn:
        Base.metadata.create_all(bind=conn)


def get_db() -> Session:
    with Session() as session:
        yield session
