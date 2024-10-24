import mysql.connector

con =mysql.connector.connect(
    user="root",
    host="localhost",
    database="alx_book_store",
    passwd="#Lerato0903"
)
print(con)