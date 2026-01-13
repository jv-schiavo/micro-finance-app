import tkinter as tk
from tkinter import ttk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def build_reports_view(parent, app_context):
    frame = tk.Frame(parent)
    app_context["frames"]["reports"] = frame
    frame.grid(row=0, column=0, sticky="nsew")

    report_service = app_context["services"]["report"]

    tk.Label(frame, text="Reports & Dashboard", font=("Arial", 18, "bold")).pack(pady=10)
    tk.Button(frame, text="Return",width=15, command=lambda: app_context["frames"]["main"].tkraise()).pack(pady=10)

    dashboard_frame = tk.LabelFrame(frame, text="Dashboard", padx=10, pady=10)
    dashboard_frame.pack(fill="x", padx=15, pady=10)

    kpi_var = tk.StringVar(value="total_amount")

    kpi_frame = tk.Frame(dashboard_frame)
    kpi_frame.pack(anchor="w", padx=10, pady=5)

    tk.Radiobutton(
        kpi_frame,
        text="Total Amount Issued",
        variable=kpi_var,
        value="total_amount"
    ).pack(side="left", padx=5)

    tk.Radiobutton(
        kpi_frame,
        text="Total Loans",
        variable=kpi_var,
        value="total_loans"
    ).pack(side="left", padx=5)

    tk.Radiobutton(
        kpi_frame,
        text="Average Loan Amount",
        variable=kpi_var,
        value="avg_amount"
    ).pack(side="left", padx=5)

    fig = Figure(figsize=(8, 3.5), dpi=100)
    ax = fig.add_subplot(111)

    canvas = FigureCanvasTkAgg(fig, master=dashboard_frame)
    canvas.get_tk_widget().pack(padx=10, pady=5)
    canvas.draw()

    def refresh_chart():
        ax.clear()

        rows = report_service.get_dashboard_data()

        products = [r["product_name"] for r in rows]

        if kpi_var.get() == "total_amount":
            values = [r["total_amount_issued"] for r in rows]
            title = "Total Amount Issued by Product"
            ylabel = "Amount"

        elif kpi_var.get() == "total_loans":
            values = [r["total_loans"] for r in rows]
            title = "Total Loans by Product"
            ylabel = "Loans"

        else:
            values = [r["avg_loan_amount"] for r in rows]
            title = "Average Loan Amount by Product"
            ylabel = "Amount"

        ax.bar(products, values)
        ax.set_title(title)
        ax.set_ylabel(ylabel)
        ax.set_xlabel("Product")
        ax.tick_params(axis="x", rotation=25)

        fig.tight_layout()
        canvas.draw()
    
    for widget in kpi_frame.winfo_children():
        widget.config(command=refresh_chart)

    refresh_chart()

    # REPORT 
    report_frame = tk.LabelFrame(frame, text="Loan Report", padx=10,pady=10)
    report_frame.pack(fill="both", expand=True, padx=15, pady=10)

    build_loan_report_table(report_frame, report_service)    

def build_loan_report_table(parent, report_service):
    columns = (
        "loan_id",
        "customer",
        "product",
        "application_date",
        "approval_date",
        "principal",
    )

    tree = ttk.Treeview(parent, columns=columns, show="headings", height=10)

    tree.heading("loan_id", text="Loan ID")
    tree.heading("customer", text="Customer")
    tree.heading("product", text="Product")
    tree.heading("application_date", text="Application Date")
    tree.heading("approval_date", text="Approval Date")
    tree.heading("principal", text="Principal")

    tree.column("loan_id", width=80, anchor="center")
    tree.column("customer", width=160, anchor="center")
    tree.column("product", width=140, anchor="center")
    tree.column("application_date", width=130, anchor="center")
    tree.column("approval_date", width=130, anchor="center")
    tree.column("principal", width=120, anchor="center")

    tree.pack(fill="both", expand=True)

    load_loan_report(tree, report_service)


def load_loan_report(tree, report_service):
    tree.delete(*tree.get_children())

    rows = report_service.get_loan_report()

    for row in rows:
        tree.insert(
            "",
            "end",
            values=(
                row["loan_id"],
                row["name"],
                row["product_name"],
                row["applicationDate"],
                row["approval_date"],
                row["principalAmount"],
            )
        )
