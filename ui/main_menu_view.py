import tkinter as tk

def build_main_menu_view(parent, app_context):
    frame = tk.Frame(parent)
    app_context["frames"]["main"] = frame

    frame.grid(row=0, column=0, sticky="nsew")

    tk.Label(frame, text="Main Menu", font=("Arial", 18, "bold")).pack()

    spacer = tk.Frame(frame)
    spacer.pack(fill="both", expand=True)

    # Logout flow
    def on_logout_click():
        app_context["frames"]["login"].tkraise()
    
    tk.Button(frame, text="Logout", width=15, command=on_logout_click).pack(anchor="se", padx=15, pady=15)

    # Products flow
    def on_products_click():
        app_context["frames"]["products"].tkraise()

    tk.Button(frame, text="Products", width=15, command=on_products_click).pack(pady=10)

    # Repayment flow
    def on_repayments_click():
        app_context["frames"]["repayments"].tkraise()

    tk.Button(frame, text="Repayments", width=15, command=on_repayments_click).pack(pady=15)    

    # Application flow
    def on_application_click():
        app_context["frames"]["applications"].tkraise()

    tk.Button(frame, text="Applications", width=15, command=on_application_click).pack(pady=5)

    # Reports flow
    def on_repots_click():
        app_context["frames"]["reports"].tkraise()

    tk.Button(frame, text="Reports", width=15, command=on_repots_click).pack(pady=5)


   

