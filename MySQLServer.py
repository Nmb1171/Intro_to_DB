import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'CLASHROYALe032001*' 
    )

    if connection.is_connected():
        cursor = connection.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error:
    print("Error:", mysql.connector.Error)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")