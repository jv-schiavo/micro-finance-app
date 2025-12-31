import tkinter as tk
from tkinter import ttk
from datetime import *

def build_repayments_view(parent, app_context):
    frame = tk.Frame(parent)
    app_context["frames"]["repayments"] = frame

    frame.grid(row=0, column=0, sticky="nsew")

    tk.Label(frame, text="Repayments", font=("Arial", 18, "bold")).pack()

   
    # Loan Selection
    loan_bar = tk.Frame(frame)
    loan_bar.pack(anchor="nw", pady=20)

    tk.Label(loan_bar, text="Loan:", font=("Arial", 12, "bold")).pack(side="left", padx=5)

    loan_var = tk.StringVar()

    loan_combo = ttk.Combobox(
        loan_bar,
        textvariable=loan_var,
        state="readonly",
        width=40
    )
    loan_combo.pack(side="left")

     # Temp Loan opt
    loans = [
        (1, "LN-000234", "John Smith", 5000, "ACTIVE"),
        (2, "LN-000235", "John Smith", 2000, "CLOSED"),
        (3, "LN-000236", "Mary Jones", 3500, "ACTIVE"),
    ] 
    
    loan_map = {}

    display_values = []

    for loan_id, loan_code, name, amount, status in loans:
        display = f"{loan_code} | {name} | £{amount} | {status}"
        display_values.append(display)
        loan_map[display] = loan_id

    loan_combo["values"] = display_values

    def get_selected_loan():
        selected = loan_var.get()
        return loan_map.get(selected)
    
    info_label = tk.Label(
    loan_bar,
    textvariable=loan_var,
    font=("Arial", 10,"bold"))
    info_label.pack(anchor="w", padx=15, pady=10)

    # Debugger
    def on_loan_selected(event):
        loan = get_selected_loan()
        return loan

    loan_combo.bind("<<ComboboxSelected>>", on_loan_selected)


    # Period Filter
    period_bar = tk.Frame(frame)
    period_bar.pack(anchor="nw")

    tk.Label(period_bar, text="Period:", font=("Arial", 12, "bold")).pack(side="left", padx=5)

    period_var = tk.StringVar()

    period_combo = ttk.Combobox(
        period_bar,
        textvariable=period_var,
        state="readonly",
        width=38
    )
    period_combo.pack(side="left")

    periods = [
        (""),
        ("This month"),
        ("Last month"),
        ("Last 3 months"),
        ("All")
        
    ]
    
    period_combo["values"] = periods

    def get_selected_period():
        selected = period_var.get()

        today = date.today()

        if selected == "This month":
            start = today.replace(day=1)
            end = today
            print(start, end)

        elif selected == "Last month":
            first_day_this_month = today.replace(day=1)
            end = first_day_this_month - timedelta(days=1)
            start = end.replace(day=1)
            print(start, end)

        elif selected == "Last 3 months":
            start = today - timedelta(days=90)
            end = today
            print(start, end)

        elif selected == "All":
            start = today - timedelta(days=1825)
            end = today
            print(start, end)

        elif selected == "":
            start = None
            end = None
            print()

        return start, end  


    def on_period_selected(event):
        start, end = get_selected_period()
        if start and end:
            period_var.set(f"From {start} To {end}")

    period_label = tk.Label(
    period_bar,
    textvariable=period_var,
    font=("Arial", 10, "bold"))
    period_label.pack(padx=25)

        
    period_combo.bind("<<ComboboxSelected>>", on_period_selected)

    # Button to add repayments manually
    add_repayment_holder = tk.Frame(frame)
    add_repayment_holder.pack(anchor="w",padx=8, pady=2)

    # Creating Table
    table_frame = tk.Frame(frame)
    table_frame.pack(fill="both", expand=True, padx=15, pady=10)

    columns = ("repayment id", "date", "amount", "method", "reference")

    tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

    tree.heading("repayment id", text="ID")
    tree.heading("date", text="Date")
    tree.heading("amount", text="Amount")
    tree.heading("method", text="Method")
    tree.heading("reference", text="Reference")

    tree.column("repayment id", width=50, anchor="center")
    tree.column("date", width=180, anchor="center")
    tree.column("amount", width=100, anchor="center")
    tree.column("method", width=100)
    tree.column("reference", width=100)

    tree.pack(fill="both", expand=True, padx=15, pady=10)
    

    def on_add_application():
        popup = tk.Toplevel(frame)
        popup.title("Add Repayment")
        popup.geometry("350x550")
        popup.transient(frame)
        popup.grab_set()

        tk.Label(popup, text="Amount").pack(pady=5)
        amount_entry = tk.Entry(popup)
        amount_entry.pack()

        tk.Label(popup, text="Method").pack(pady=5)
        method_entry = tk.Entry(popup)
        method_entry.pack()

        tk.Label(popup, text="Reference").pack(pady=5)
        reference_entry = tk.Entry(popup)
        reference_entry.pack()

        def save_application():
            amount = amount_entry.get()
            method = method_entry.get()
            reference = reference_entry.get()
            today = date.today()

            if not (amount and method and reference):
                return
            
            tree.insert("", "end", values=("", today, amount, method, reference))
            popup.destroy()

        tk.Button(popup, text="Save", width=10, command=save_application).pack(pady=15) 
    
    tk.Button(add_repayment_holder, text="Add Repayment", width=15, command=on_add_application).pack(anchor="w",padx=8, pady=20)

    receipt_frame = tk.LabelFrame(frame, text="Receipt / Details", padx=10, pady=10)
    receipt_frame.pack(fill="x", padx=15, pady=10)

    tk.Label(receipt_frame, text="Select a repayment to view details").pack()




    




     # Return flow
    def on_return_click():
        app_context["frames"]["main"].tkraise()
    
    footer = tk.Frame(frame)
    footer.pack(fill="x", padx=15, pady=10)
    tk.Button(footer, text="Return", width=15, command=on_return_click).pack(anchor="se")
