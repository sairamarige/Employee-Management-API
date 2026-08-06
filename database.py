import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker,declarative_base


load_dotenv()

DATABASE_URL=os.getenv("DB_URL")



engine=create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()

#provides a base class for models of sql tables 
