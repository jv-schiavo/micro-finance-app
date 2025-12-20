import tkinter as tk

def build_main_menu_view(parent, app_context):
    frame = tk.Frame(parent)
    app_context["frames"]["main"] = frame
    frame.grid(row=0, column=0, sticky="nsew")

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
    
    menu_button("Products",
        lambda: app_context["frames"]["products"].tkraise()).pack(pady=6)

    menu_button("Repayments",
        lambda: app_context["frames"]["repayments"].tkraise()).pack(pady=6)

    menu_button("Reports",
        lambda: app_context["frames"]["reports"].tkraise()).pack(pady=6)

    # Logout
    tk.Button(frame, text="Logout", width=12, command=lambda: app_context["frames"]["login"].tkraise()).place(relx=0.97, rely=0.05, anchor="ne")
