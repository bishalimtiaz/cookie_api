# cookie_api
Fast API Startup Template

### upgrade pip
`python -m pip install --upgrade pip`

### Run Project
Use bash command

`ENV=dev uvicorn app.main:app` to start dev environment <br />
`ENV=prod uvicorn app.main:app` to start prod environment <br />

## Development Instruction
To create new table create `a_model.py` inside `models` package. Then create a class that will define a `Table` inside db.

```
class A(Base):
    __tablename__ = "a"

    id = Column(Integer, primary_key=True)
    data = Column(String)
    create_date = Column(DateTime, server_default=func.now())
    bs = relationship("B")

    # required in order to access columns with server defaults
    # or SQL expression defaults, subsequent to a flush, without
    # triggering an expired load
    __mapper_args__ = {"eager_defaults": True}
```

Will User SqlAlchemy for relational database. You can Read more from here<br />
https://docs.sqlalchemy.org/en/14/orm/tutorial.html<br/>
https://docs.sqlalchemy.org/en/14/dialects/index.html<br/>
https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#asyncio-install<br/>
https://docs.sqlalchemy.org/en/14/orm/session_basics.html<br/>
https://docs.sqlalchemy.org/en/14/core/engines.html<br/>

## Library Documentation
* passlib: Passlib is a password hashing library <br/> https://passlib.readthedocs.io/en/stable/

