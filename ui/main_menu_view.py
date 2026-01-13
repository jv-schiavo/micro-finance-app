import tkinter as tk
from tkinter import messagebox

def build_main_menu_view(parent, app_context):
    frame = tk.Frame(parent)
    app_context["frames"]["main"] = frame
    frame.grid(row=0, column=0, sticky="nsew")

    auth_service = app_context["services"]["auth"]

    # Center container
    content = tk.Frame(frame)
    content.place(relx=0.5, rely=0.5, anchor="center")

    # Title
    tk.Label(content, text="Main Menu", font=("Arial", 22, "bold")).pack(pady=(0, 25))

    # Button style
    def menu_button(text, command):
        return tk.Button(content, text=text, width=25, height=2, command=command)
    
    # Menu buttons
    menu_button("Applications",
        lambda: app_context["frames"]["applications"].tkraise()).pack(pady=6)
    
    menu_button("Customers",
                lambda: app_context["frames"]["customers"].tkraise()).pack(pady=6)
    
    menu_button("Loans",
                lambda: app_context["frames"]["loans"].tkraise()).pack(pady=6)
    
    menu_button("Products",
        lambda: app_context["frames"]["products"].tkraise()).pack(pady=6)

    menu_button("Repayments",
        lambda: app_context["frames"]["repayments"].tkraise()).pack(pady=6)

    menu_button("Reports",
        lambda: app_context["frames"]["reports"].tkraise()).pack(pady=6)
    
    def logout():
        app_context["session"]["user"] = None
        app_context["frames"]["login"].tkraise()


    # Logout
    top_right = tk.Frame(frame)
    top_right.place(relx=0.97, rely=0.05, anchor="ne")

    tk.Button(top_right, text="Logout", width=12, command=logout).pack(pady=(0, 5))
    

    # Register user
    def register_user():
        popup = tk.Toplevel(frame)
        popup.title("Register User")
        popup.geometry("350x250")
        popup.transient(frame)
        popup.grab_set()

        tk.Label(popup, text="Username").pack(pady=5)
        username_entry = tk.Entry(popup)
        username_entry.pack()

        tk.Label(popup, text="Password").pack(pady=5)
        password_entry = tk.Entry(popup, show="*")
        password_entry.pack()

        def save_register():
                auth_service.register_user(
                    username_entry.get(),
                    password_entry.get())
                popup.destroy()
            
        tk.Button(popup, text="Save", width=10, command=save_register).pack(pady=15)
    
    tk.Button(top_right, text="Register", width=12, command=register_user).pack()

