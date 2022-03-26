import sqlalchemy
from sqlalchemy.orm import sessionmaker

# SQLAlchemy specific code, as with any other app
# DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = "postgresql://postgres:root@localhost/celery-db"


metadata = sqlalchemy.MetaData()

notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("task_name", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.String),
)


engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

connection = engine.connect()

insert_query = notes.insert().values([
    {'task_name' : 'oo_function', 'status' :'started'},
    {'task_name' : 'another_anone', 'status' :'processing'},
])

connection.execute(insert_query)