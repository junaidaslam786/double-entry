from database import Database
import os
from src.config import db_config

# # Load environment variables from .env file
# load_dotenv()

# # Database configuration
# db_config = {
#     'user': os.getenv('DB_USER'),
#     'password': os.getenv('DB_PASSWORD'),
#     'host': os.getenv('DB_HOST'),
#     'port': os.getenv('DB_PORT'),
#     'database': os.getenv('DB_DATABASE')
# }

# # Initialize the database class
# db = Database(db_config)
# db.initialize_connection_pool()

def create_tables(db):
    # SQL for creating the Accounts table
    create_accounts_table_sql = """
    CREATE TABLE IF NOT EXISTS accounts (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        balance DECIMAL NOT NULL
    );
    """

    # SQL for creating the Transactions table
    create_transactions_table_sql = """
    CREATE TABLE IF NOT EXISTS transactions (
        id SERIAL PRIMARY KEY,
        date TIMESTAMP NOT NULL,
        description TEXT NOT NULL
    );
    """

    # SQL for creating the Transaction Details table
    create_transaction_details_table_sql = """
    CREATE TABLE IF NOT EXISTS transaction_details (
        id SERIAL PRIMARY KEY,
        transaction_id INTEGER REFERENCES transactions(id),
        account_id INTEGER REFERENCES accounts(id),
        amount DECIMAL NOT NULL,
        type TEXT CHECK (type IN ('Debit', 'Credit'))
    );
    """

    # Execute the SQL statements
    db.execute_query(create_accounts_table_sql)
    db.execute_query(create_transactions_table_sql)
    db.execute_query(create_transaction_details_table_sql)

# Call the create_tables function
if __name__ == "__main__":
    db = Database(db_config)
    db.initialize_connection_pool()
    create_tables(db)
    db.close_all_connections()