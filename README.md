# cookie_api
Fast API Startup Template

### upgrade pip
`python -m pip install --upgrade pip` if you want to upgrade the pip version for your project

### Run Project
Use bash command from root directory

`ENV=dev uvicorn app.main:app` to start dev environment or `uvicorn app.main:app`  that will start dev environment<br />
`ENV=prod uvicorn app.main:app` to start prod environment <br />

Then go to app directory `cd app` and run `python create_food_data.py`. It will create food data from excel file. This command must run once and if it is run multiple time it will create multiple Entry.

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

SqlAlchemy is used for relational database. You can Read more from here<br />
https://docs.sqlalchemy.org/en/14/orm/tutorial.html<br/>
https://docs.sqlalchemy.org/en/14/dialects/index.html<br/>
https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#asyncio-install<br/>
https://docs.sqlalchemy.org/en/14/orm/session_basics.html<br/>
https://docs.sqlalchemy.org/en/14/core/engines.html<br/>

## Library Documentation
* passlib: Passlib is a password hashing library <br/> https://passlib.readthedocs.io/en/stable/

