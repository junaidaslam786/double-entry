from database import Database
import os
from src.config import db_config

def create_tables(db):
    # SQL for creating the Teacher table
    create_teacher_table_sql = """
    CREATE TABLE IF NOT EXISTS teacher (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        subject VARCHAR(255) NOT NULL
    );
    """

    # SQL for creating the Class table
    create_class_table_sql = """
    CREATE TABLE IF NOT EXISTS class (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        teacher_id INT,
        FOREIGN KEY (teacher_id) REFERENCES teacher(id)
    );
    """

    # SQL for creating the Student table
    create_student_table_sql = """
    CREATE TABLE IF NOT EXISTS student (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        grade VARCHAR(50) NOT NULL
    );
    """

    # SQL for creating the ClassStudent junction table
    create_class_student_table_sql = """
    CREATE TABLE IF NOT EXISTS class_student (
        id INT AUTO_INCREMENT PRIMARY KEY,
        class_id INT,
        student_id INT,
        FOREIGN KEY (class_id) REFERENCES class(id),
        FOREIGN KEY (student_id) REFERENCES student(id)
    );
    """

    # Execute the SQL statements
    db.execute_query(create_teacher_table_sql)
    db.execute_query(create_class_table_sql)
    db.execute_query(create_student_table_sql)
    db.execute_query(create_class_student_table_sql)

# Call the create_tables function
if __name__ == "__main__":
    db = Database(db_config)
    db.initialize_connection_pool()
    create_tables(db)
    print("Tables created successfully.")
    db.release_connection()
