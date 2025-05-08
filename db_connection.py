# db_connection.py
from langchain.utilities import SQLDatabase
from sqlalchemy import create_engine

# Replace with your RDS info
DB_HOST = ""
DB_PORT = 3306
DB_NAME = ""
DB_USER = ""
DB_PASS = ""

def get_database():
    engine_url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}""?charset=utf8mb4"
    return SQLDatabase.from_uri(engine_url)

