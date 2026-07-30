from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker,declarative_base

# DATABASE_URL="mysql+pymysql://root:1234@localhost:3306/store_db"
DATABASE_URL="mysql+pymsql://avnadmin:AVNS_ltzGQHRHtNxWPlp03iq@mysql-1d69e83f-sairamarige2140-f01e.c.aivencloud.com:16747/defaultdb"

engine=create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()

#provides a base class for models of sql tables 
