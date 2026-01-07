import tkinter as tk
from tkinter import ttk

def build_reports_view(parent, app_context):
    frame = tk.Frame(parent)
    app_context["frames"]["reports"] = frame

    frame.grid(row=0, column=0, sticky="nsew")

    tk.Label(frame, text="Dashboard & Report", font=("Arial", 18, "bold")).pack()

    dashboard_frame = tk.LabelFrame(frame, text="Loan Overview")
    dashboard_frame.pack()

    # Dashboard Table
    dashboard_tree = ttk.Treeview(dashboard_frame, columns=("product", "total", "sum", "avg"), show="headings", height=10)

    dashboard_tree.heading("product", text="Product")
    dashboard_tree.heading("total", text="Total Loans")
    dashboard_tree.heading("sum", text="Total Issued")
    dashboard_tree.heading("avg", text="Average Loan")

    dashboard_tree.pack(fill="x")


    ## separator

    ## filter ui to be done here

    filter_frame = tk.Frame(frame)
    filter_frame.pack(fill="x", padx=15, pady=10)

    # product filter
    product_frame = tk.Frame(filter_frame)
    product_frame.pack(side="left", padx=10)

    tk.Label(product_frame, text="Product", font=("Arial", 12)).pack()

    product_var = tk.StringVar()
    
    products_combo = ttk.Combobox(product_frame,textvariable=product_var, state="readonly", width=40)
    products_combo.pack()

    products = [
        ("Loan"),
        ("Another loan"),
        ("Loan Again"),
        ("All")
        
    ]
    
    products_combo["values"] = products
    products_combo.set("")


    # Status Filter
    status_frame = tk.Frame(filter_frame)
    status_frame.pack(side="left", padx=10)

    tk.Label(status_frame, text="Status", font=("Arial", 12)).pack()
    status_var = tk.StringVar()
    status_combo = ttk.Combobox(status_frame,textvariable=status_var, state="readonly", width=40)
    status_combo.pack()

    status_var = tk.StringVar()

    status =  [
        "All",
        "ACTIVE",
        "CLOSED"
    ]

    status_combo["values"] = status
    status_combo.set("")

    

    report_frame = tk.LabelFrame(frame, text="Loan Report")
    report_frame.pack(fill="both", expand=True, padx=15, pady=10)

    # Report Table
    report_tree = ttk.Treeview(report_frame, columns=("loan_id", "name", "phone", "product", "app_date", "approval_date", "amount", "status"), show="headings",height=10)

    report_tree.heading("loan_id", text="Loan ID")
    report_tree.heading("name", text="Name")
    report_tree.heading("phone", text="Phone Number")
    report_tree.heading("product", text="Product Name")
    report_tree.heading("app_date", text="Application Date")
    report_tree.heading("approval_date", text="Date of Approval")
    report_tree.heading("amount", text="Loan Amount")
    report_tree.heading("status", text="Loan Status")

    report_tree.pack(fill="both", expand=True)


    # Return flow
    def on_return_click():
        app_context["frames"]["main"].tkraise()
    
    tk.Button(frame, text="Return", width=15, command=on_return_click).pack(anchor="se", padx=15, pady=15)