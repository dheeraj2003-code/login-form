import tkinter as tk
from tkinter import messagebox
USERNAME = "admin"
PASSWORD = "password123"

def login():
    user = username_entry.get()
    password = password_entry.get()
    
    if user == USERNAME and password == PASSWORD:
        messagebox.showinfo("Login Successful", f"Welcome, {user}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
#gui 
root = tk.Tk()
root.title("Login")
root.geometry("300x180")

tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()