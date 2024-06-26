import sys
import os
import tkinter as tk

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.ui.app_ui import DashboardApp
from src.database.database import Database
from src.database.create_tables import create_tables
from src.config import db_config
# Import other necessary modules or functions, if any

def main():
    # Initialize the Database
    db = Database(db_config)
    try:
        db.initialize_connection_pool()
        print("Database connection pool initialized successfully.")

        # Create tables
        create_tables(db)

    except Exception as e:
        print(f"Failed to initialize database connection pool: {e}")
        return

    # Launch the UI of the application
    root = tk.Tk()
    app = DashboardApp(root, db)
    root.mainloop()

if __name__ == "__main__":
    main()
