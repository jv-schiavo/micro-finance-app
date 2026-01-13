import tkinter as tk
from tkinter import ttk

def build_loan_view(parent, app_context):
    frame = tk.Frame(parent)
    app_context["frames"]["loans"] = frame
    frame.grid(row=0, column=0, sticky="nsew")

    loan_service = app_context["services"]["loan"]
    
    content = tk.Frame(frame)
    content.place(relx=0.5, rely=0.5, anchor="center")
   
    tk.Label(frame, text="Loans", font=("Arial", 18, "bold")).pack(anchor="w", padx=15, pady=(10,5))

    search_frame = tk.Frame(frame)
    search_frame.pack(anchor="w", padx=15, pady=5)

    tk.Label(search_frame, text="Search:").pack(side="left")
    search_entry = tk.Entry(search_frame, width=30)
    search_entry.pack(side="left", padx=5)

    # Create table
    columns = ("id", "name", "disburcement date", "outstanding balance", "total")

    tree = ttk.Treeview(frame, columns=columns, show="headings", height=25)

    tree.heading("id", text="ID")
    tree.heading("name", text="Customer Name")
    tree.heading("disburcement date", text="Disburcement Date")
    tree.heading("outstanding balance", text="Outstanding Balance")
    tree.heading("total", text="Total payable")

    tree.column("id", width=10)
    tree.column("name", anchor="center")
    tree.column("disburcement date", anchor="center")
    tree.column("outstanding balance", anchor="center")
    tree.column("total", anchor="center")

    tree.pack(fill="both", expand=True, padx=15, pady=10)

    def load_loan():
        tree.delete(*tree.get_children())

        rows = loan_service.get_all_loans()

        for row in rows:
            tree.insert("", "end", values=(
                    row["loan_id"],
                    row["name"],
                    row["disbursementDate"],
                    row["outstandingBalance"],
                    row["total_payable"]
                ))


    def on_return_click():
        # No auth yet. Just prove navigation works.
        app_context["frames"]["main"].tkraise()

    load_loan()
    tk.Button(frame, text="Return", width=15, command=on_return_click).pack(anchor="se", padx=15, pady=15)

    


