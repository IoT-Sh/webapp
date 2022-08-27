from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import databases 
import os

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/webapp"
database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL, pool_size=3, max_overflow=0)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()



