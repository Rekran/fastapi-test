# Configurações do banco de dados
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
from models import Item
from dotenv import load_dotenv
import os

load_dotenv()


POSTGRES_USER = os.getenv("SQL_USER")
POSTGRES_PASSWORD = os.getenv("SQL_PASSWORD")
POSTGRES_DB = os.getenv("SQL_NAME")
POSTGRES_HOST = os.getenv("SQL_HOST")
POSTGRES_PORT = os.getenv("SQL_PORT")


SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def upload_csv(filename: str):
    db = SessionLocal()
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                item = Item(name=row['name'], description=row['description'])
                db.add(item)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()