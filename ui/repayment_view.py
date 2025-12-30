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

    def get_selected_loan_id():
        selected = loan_var.get()
        return loan_map.get(selected)
    
    # Debugger
    def on_loan_selected(event):
        loan_id = get_selected_loan_id()
        print("Selected loan_id:", loan_id)

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
            


        return periods.index(selected)
    
    # Debugger
    def on_period_selected(event):
        period = get_selected_period()
        print("Selected period:", period)

    period_combo.bind("<<ComboboxSelected>>", on_period_selected)


     # Return flow
    def on_return_click():
        app_context["frames"]["main"].tkraise()
    
    footer = tk.Frame(frame)
    footer.pack(fill="x", padx=15, pady=10)
    tk.Button(footer, text="Return", width=15, command=on_return_click).pack(anchor="se")
