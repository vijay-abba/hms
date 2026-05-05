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

    @staticmethod
    def get_connection():
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

    @staticmethod
    def close(conn, cursor=None):
        if cursor:
            cursor.close()
            print("Connection closed for cursor")
        if conn and conn.is_connected():
            conn.close()
            print("Connection closed for conn")



conn = DBConnection.get_connection()
print(conn)
DBConnection.close(conn)
