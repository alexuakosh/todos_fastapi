from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config


SQLALCHEMY_DATABASE_URL = config('DB')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


