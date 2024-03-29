import os
from dotenv import load_dotenv
import mysql.connector

# Get values from .env
load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Connection to MySQL server
connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD
)

# Cursor object creation for SQL-requests
cursor = connection.cursor()

# Database creation
cursor.execute("CREATE DATABASE IF NOT EXISTS immo_prices")
print("Database immo_prices created successfully")

# Connection to created DB
cursor.execute("USE immo_prices")

# Table regions creation
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS regions (
    name VARCHAR(50) NOT NULL PRIMARY KEY,
    INDEX idx_name (name)
    )
""")
print("Table regions created successfully")

# Table departments creation
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS departments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    code INT(3) NOT NULL,
    region_name VARCHAR(50) NOT NULL,
    price_per_square_meter FLOAT NOT NULL,
    FOREIGN KEY(region_name) REFERENCES regions(name),
    INDEX idx_code (code)
    )
""")
print("Table departments created successfully")

# Table cities creation
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cities (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        code VARCHAR(10) NOT NULL,
        department_code INT NULL,
        price_per_square_meter FLOAT NOT NULL,
        FOREIGN KEY (department_code) REFERENCES departments(code)
    )
""")
print("Table cities created successfully")

# Close connection to DB
cursor.close()
connection.close()
