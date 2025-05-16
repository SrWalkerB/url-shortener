import os
from sqlmodel import create_engine, SQLModel, Session

class Database:
    sql_url = ''
    db_name = ''
    engine = None

    def __init__(self):
        db_user = os.getenv('POSTGRES_USER')
        db_password = os.getenv('POSTGRES_PASSWORD')
        db_port = os.getenv('POSTGRES_PORT')
        db_name = os.getenv('POSTGRES_DB') 
        db_host = os.getenv('POSTGRES_HOST')

        self.sql_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
        self.db_name = db_name
        self.on_init()

    def on_init(self):
        engine = create_engine(self.sql_url)

        SQLModel.metadata.create_all(engine)

        self.engine = engine
        print(f'On connected {self.db_name}')
    
    def get_engine(self):
        return self.engine

    def get_session(self):
        session = Session(self.engine)

        return session
