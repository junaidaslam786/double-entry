import tkinter as tk
from tkinter import ttk

from .add_student import AddStudentForm

class DashboardApp:
    def __init__(self, root, db):
        self.root = root
        self.db = db 
        self.root.title("Dashboard")
        self.root.geometry("800x600")  # Set the size of the app window

        # Create app bar at the top
        self.app_bar = ttk.Frame(root, height=50, padding=5)
        self.app_bar.pack(fill=tk.X, side=tk.TOP)
        
        # Links in the app bar
        self.add_links_to_app_bar()

        # Content area
        self.content_area = ttk.Frame(root, padding=5)
        self.content_area.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # Create footer at the bottom
        self.footer = ttk.Frame(root, height=30, padding=5)
        self.footer.pack(fill=tk.X, side=tk.BOTTOM)
        self.footer_label = ttk.Label(self.footer, text="Footer messages", font=("Arial", 12))
        self.footer_label.pack(side=tk.RIGHT)


    def add_links_to_app_bar(self):
        ttk.Button(self.app_bar, text="Add Student", command=self.show_add_student_form).pack(side=tk.LEFT)
        ttk.Button(self.app_bar, text="Add Teachers").pack(side=tk.LEFT)
        ttk.Button(self.app_bar, text="Create a Class").pack(side=tk.LEFT)

    def show_add_student_form(self):
        # Open a new window for the Add Customer form
        new_window = tk.Toplevel(self.root)
        add_student_form = AddStudentForm(new_window, self.db)

def main():
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
