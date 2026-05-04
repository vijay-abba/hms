import mysql.connector
from mysql.connector import Error

from exceptions.custom_exceptions import DatabaseConnectionError

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Phani@225",
    "database": "hms",
}


class DBConnection:

    def get_connection(self):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            if conn.is_connected():
                print("Connected to Database Successfully ")
                return conn
            raise DatabaseConnectionError(
                "Connection Object is created but not connected"
            )
        except Error as e:
            raise DatabaseConnectionError(f"MySQL error : {e}")


dbObj = DBConnection()
dbObj.get_connection()