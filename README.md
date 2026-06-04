# Inventory-Management-App
A full-stack Inventory Management System built with FastAPI and MySQL.
Tech Stack

FastAPI — Python backend
MySQL — database
SQLAlchemy — ORM for database interaction
HTML/CSS/JS — frontend UI

Features

Add, Edit, Delete products
Real-time search by ID, name or description
Data persisted in MySQL database
Clean and responsive UI

How to Run
1. Clone the repository
git clone https://github.com/myselfzain95-coder/Inventory-Management-App.git
2. Create and activate virtual environment
python -m venv myenv
myenv\Scripts\activate
3. Install dependencies
pip install fastapi uvicorn sqlalchemy mysql-connector-python
4. Create the database in MySQL
CREATE DATABASE inventory_db;
5. Update database credentials in database.py
6. Run the app
uvicorn main:app --reload
7. Open index.html in your browser
   
API Endpoints
GET /products
Retrieves all products from the database.
POST /products
Creates a new product by accepting name, description, price and quantity.
PUT /products/{id}
Updates an existing product by its ID.
DELETE /products/{id}
Deletes a product from the database by its ID.
