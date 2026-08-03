Employee Management API
========================

A FastAPI + SQLAlchemy backend for managing employee records, with
role-based access control (intern / dev / manager).


Project Files
--------------
main.py        - FastAPI app and route definitions
models.py      - SQLAlchemy ORM models (Employee, User)
schemas.py     - Pydantic request/response schemas
crud.py        - Database operations + auth helpers (hashing, JWT)
auth.py        - JWT decoding + role-based access dependencies
database.py    - DB engine/session setup (create this yourself, see below)
requirements.txt - Python package dependencies


Roles & Permissions
--------------------
Every user has a role: intern, dev, or manager.

  intern   -> GET only
  dev      -> GET, POST, PUT, PATCH
  manager  -> GET, POST, PUT, PATCH, DELETE

Role is checked from the JWT cookie set at login.


Setup Instructions
--------------------

1. Create a virtual environment

   python -m venv venv

   Activate it:
     Windows:      venv\Scripts\activate
     macOS/Linux:  source venv/bin/activate

2. Install dependencies

   pip install -r requirements.txt

3. Create database.py (if you don't already have one)

   from sqlalchemy import create_engine
   from sqlalchemy.orm import sessionmaker, declarative_base
   import os
   from dotenv import load_dotenv

   load_dotenv()

   DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://user:password@localhost/employee_db")

   engine = create_engine(DATABASE_URL)
   SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
   Base = declarative_base()

   If you don't have MySQL set up, use SQLite instead (no server needed):

   DATABASE_URL = "sqlite:///./employee.db"

   (and remove PyMySQL-specific parts if you go this route)

4. Create a .env file in the project root

   DATABASE_URL=mysql+pymysql://your_mysql_user:your_mysql_password@localhost/employee_db
   SECRET_KEY=replace-this-with-a-long-random-string

   If using MySQL, create the database first:
     CREATE DATABASE employee_db;

5. Run the server

   python -m uvicorn main:app --reload

   (Use "python -m uvicorn" instead of just "uvicorn" if the standalone
   uvicorn.exe launcher gets blocked by an Application Control / AppLocker
   policy on your machine.)

6. Open the interactive docs

   http://127.0.0.1:8000/docs


Basic Usage
--------------------

Register a user:
  POST /register_user
  { "username": "...", "password": "...", "email": "...", "role": "manager" }

Log in (sets an access_token cookie):
  POST /login
  { "email": "...", "password": "..." }

Then use the other endpoints (/employees, /department/{name}, etc.)
The cookie from login determines what your role is allowed to do.

























