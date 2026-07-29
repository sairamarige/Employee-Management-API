🛍️ FastAPI Store Management 

A RESTful Store Management API built with FastAPI, SQLAlchemy, and MySQL. This project demonstrates how to build a scalable backend application using clean architecture while implementing complete CRUD (Create, Read, Update, Delete) operations for multiple product categories.



🚀 Features:

- RESTful API built with FastAPI
- SQLAlchemy ORM for database operations
- MySQL database integration using PyMySQL
- Pydantic models for request and response validation
- Complete CRUD operations
- Automatic interactive API documentation (Swagger UI)
- Modular project structure for easy maintenance



🛠️ Tech Stack:

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- MySQL
- PyMySQL
- Uvicorn



📁 Project Structure:

Fastapi-store-management/
│
├── main.py          # FastAPI application and API routes
├── crud.py          # CRUD database operations
├── database.py      # Database connection and session
├── models.py        # SQLAlchemy ORM models
├── schemas.py       # Pydantic schemas
├── README.md
|-- requirements.txt


⚙️ Installation:

1. Clone the Repository:

bash
git clone https://github.com/Asairam21/Fastapi-store-management.git
cd Fastapi-store-management


2. Create Virtual Environment:

Windows:
python -m venv venv
venv\Scripts\activate


Linux / macOS:
python3 -m venv venv
source venv/bin/activate


3. Install Dependencies:

pip install fastapi uvicorn sqlalchemy pymysql



🗄️ Database Configuration:

Create a MySQL database named:

store_db


Update your "database.py" file with your MySQL credentials.

DATABASE_URL = "mysql+pymysql://username:password@localhost:3306/store_db"




▶️ Run the Application:

bash
uvicorn main:app --reload


Server:
http://127.0.0.1:8000

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc



📦 API Resources:
The project manages five product categories.

| Resource | Endpoint |
|----------|----------|
| Laptops | "/laptops" |
| Mobiles | "/mobiles" |
| Food Menu | "/food-menu" |
| Furniture | "/furniture" |
| Grocery | "/grocery" |



CRUD Endpoints:
Each resource supports the following endpoints.

Create:
POST /resource


Get All:
GET /resource


Get by ID:
GET /resource/{id}


Update:
PUT /resource/{id}


Delete:
DELETE /resource/{id}


Example:

```
POST   /laptops
GET    /laptops
GET    /laptops/1
PUT    /laptops/1
DELETE /laptops/1
```

The same pattern applies to:

- "/mobiles"
- "/food-menu"
- "/furniture"
- "/grocery"



📋 Data Models:

💻 Laptop

| Field | Type |
|-------|------|
| brand | string |
| model | string |
| price | integer |
| ram_gb | integer |


📱 Mobile

| Field | Type |
|-------|------|
| brand | string |
| model | string |
| price | integer |
| storage_gb | integer |


🍔 Food Menu:

| Field | Type |
|-------|------|
| item_name | string |
| category | string |
| price | integer |
| calories | integer |


🪑 Furniture:

| Field | Type |
|-------|------|
| name | string |
| material | string |
| price | integer |
| dimensions | string |

🛒 Grocery:

| Field | Type |
|-------|------|
| item_name | string |
| category | string |
| price | integer |
| quantity | integer |



🧪 Testing:

After running the application, open:
http://127.0.0.1:8000/docs

Use the interactive Swagger UI to test all API endpoints.



🎯 Learning Outcomes

This project helped me understand:

- Building REST APIs with FastAPI
- Designing scalable backend applications
- SQLAlchemy ORM
- Database CRUD operations
- Request validation with Pydantic
- MySQL integration
- API documentation using Swagger UI
- Clean project architecture



📜 License:
This project is open source and available under the MIT License.



👨‍💻 Author

 Sai Ram

If you found this project helpful, consider giving it a ⭐ on GitHub.
