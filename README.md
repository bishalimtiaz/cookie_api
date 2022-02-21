# cookie_api
Fast API Startup Template

## upgrade pip
`python -m pip install --upgrade pip`

## Run Project
Use bash command

`ENV=dev uvicorn app.main:app` to start dev environment <br />
`ENV=prod uvicorn app.main:app` to start prod environment <br />

Will User SqlAlchemy for relational database. You can Read more from here<br />
https://docs.sqlalchemy.org/en/14/orm/tutorial.html
https://docs.sqlalchemy.org/en/14/dialects/index.html
https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#asyncio-install

