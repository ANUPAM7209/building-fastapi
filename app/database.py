import psycopg2
from psycopg2.extras import RealDictCursor  # it  is use for returning query results as dictionaries instead of tuples.
import time 

from sqlalchemy import create_engine #it 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


# SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<ip-address/hostname>/<database_name>"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL) # create an engine that will manage the connection to the postgresql.

#to talk to a database we need to create a session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() # create a base class for our models to inherit from. It will be used to create the tables in the database.

#it will create the tables in the database based on the models defined in the models.py file. It will check if the tables already exist and create them if they don't.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


