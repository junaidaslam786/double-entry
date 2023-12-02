import psycopg2
from psycopg2 import OperationalError, pool

class Database:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection_pool = None

    def initialize_connection_pool(self):
        try:
            self.connection_pool = psycopg2.pool.SimpleConnectionPool(
                1, 20,
                user=self.db_config['user'],
                password=self.db_config['password'],
                host=self.db_config['host'],
                port=self.db_config['port'],
                database=self.db_config['database']
            )
        except OperationalError as e:
            print(f"The error '{e}' occurred during connection pool initialization")
            raise

    def get_connection(self):
        return self.connection_pool.getconn()

    def release_connection(self, connection):
        self.connection_pool.putconn(connection)

    def close_all_connections(self):
        self.connection_pool.closeall()

    def execute_query(self, query, data=None):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(query, data)
            connection.commit()
            print("Query executed successfully")
        except OperationalError as e:
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
        except OperationalError as e:
            print(f"The error '{e}' occurred")
        finally:
            cursor.close()
            self.release_connection(connection)