import tkinter as tk

def build_loan_view(parent, app_context):
    frame = tk.Frame(parent)
    app_context["frames"]["loans"] = frame
    frame.grid(row=0, column=0, sticky="nsew")
    
    content = tk.Frame(frame)
    content.place(relx=0.5, rely=0.5, anchor="center")
   
    tk.Label(content, text="Loan Management", font=("Arial", 18, "bold")).pack(pady=10)

    search_frame = tk.Frame(frame)
    search_frame.pack(anchor="w", padx=15, pady=5)

    tk.Label(search_frame, text="Search:").pack(side="left")
    search_entry = tk.Entry(search_frame, width=30)
    search_entry.pack(side="left", padx=5)

    # Create table
    columns = ("id", "name", "disburcement_date", "amount", )    


    def on_return_click():
        # No auth yet. Just prove navigation works.
        app_context["frames"]["main"].tkraise()

    tk.Button(content, text="Return", width=15, command=on_return_click).pack(pady=10)

    


