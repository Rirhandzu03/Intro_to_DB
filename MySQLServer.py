import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MYSQL Server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="#Lerato0903@"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully")
    except Error as e:
        print(f"Error while connectingto MYSQL: {e}")

    finally:
        #close the conenction
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MYSQL connection is closed")

if __name__ == '__main__':
    create_database()
