import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AddStudentForm:
    def __init__(self, root, db):
        self.root = root
        self.db = db  # Database object
        self.root.title("Add Student")
        self.root.geometry("300x200")

        ttk.Label(self.root, text="Name:").grid(row=0, column=0)
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        ttk.Label(self.root, text="Grade:").grid(row=1, column=0)
        self.grade_entry = ttk.Entry(self.root)
        self.grade_entry.grid(row=1, column=1)

        ttk.Button(self.root, text="Submit", command=self.submit_form).grid(row=2, column=1)

    def submit_form(self):
        name = self.name_entry.get()
        grade = self.grade_entry.get()
        
        # Validation example
        if not name or not grade:
            messagebox.showwarning("Validation Error", "All fields are required")
            return
        
        try:
            self.db.execute_query(
                "INSERT INTO student (name, grade) VALUES (%s, %s)", 
                (name, grade)
            )
            messagebox.showinfo("Success", "Student added successfully")
            self.root.destroy()  # Optionally close the form on success
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
