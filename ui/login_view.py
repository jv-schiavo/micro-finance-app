import tkinter as tk
from tkinter import messagebox

def build_login_view(parent, app_context):
    frame = tk.Frame(parent)
    app_context["frames"]["login"] = frame
    frame.grid(row=0, column=0, sticky="nsew")
    
    content = tk.Frame(frame)
    content.place(relx=0.5, rely=0.5, anchor="center")
   
    tk.Label(content, text="Login", font=("Arial", 18, "bold")).pack(pady=10)

    tk.Label(content, text="Username").pack()

    username_entry = tk.Entry(content, width=50)
    username_entry.pack()

    tk.Label(content, text="Password").pack()

    password_entry = tk.Entry(content, show="*", width=50)
    password_entry.pack()

    def on_login_click():
        auth = app_context["services"]["auth"]

        user = auth.authenticate(username_entry.get(), password_entry.get())
        if not user:
            messagebox.showerror("Login failed", "Invalid username or password.")
            return

        app_context["session"]["user"] = user
        app_context["frames"]["main"].tkraise()

    tk.Button(content, text="Login", width=10, command=on_login_click).pack(pady=10)

    


