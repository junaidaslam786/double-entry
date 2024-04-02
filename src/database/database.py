import mysql.connector
from mysql.connector import Error, pooling

class Database:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection_pool = None

    def initialize_connection_pool(self):
        try:
            self.connection_pool = pooling.MySQLConnectionPool(
                pool_name = "mypool",
                pool_size = 20,
                pool_reset_session = True,
                user = self.db_config['user'],
                password = self.db_config['password'],
                host = self.db_config['host'],
                port = self.db_config['port'],
                database = self.db_config['database']
            )
        except Error as e:
            print(f"The error '{e}' occurred during connection pool initialization")
            raise

    def get_connection(self):
        return self.connection_pool.get_connection()

    def release_connection(self, connection):
        connection.close()

    def execute_query(self, query, data=None):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(query, data)
            connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")
            connection.rollback()
        finally:
            cursor.close()
            self.release_connection(connection)

    def execute_read_query(self, query, data=None):
        connection = self.get_connection()
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query, data)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            cursor.close()
            self.release_connection(connection)