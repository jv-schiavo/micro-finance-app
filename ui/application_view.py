import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def build_applications_view(parent, app_context):
    frame = tk.Frame(parent)
    app_context["frames"]["applications"] = frame

    frame.grid(row=0, column=0, sticky="nsew")

    application_service = app_context["services"]["application"]


    # Title
    tk.Label(frame, text="Applications", font=("Arial", 18, "bold")).pack(anchor="w", padx=15, pady=(10,5))

    toolbar = tk.Frame(frame)
    toolbar.pack(anchor="w", padx=15, pady=5)

    search_frame = tk.Frame(frame)
    search_frame.pack(anchor="w", padx=15, pady=5)
    tk.Label(search_frame, text="Search:").pack(side="left")
    search_entry = tk.Entry(search_frame, width=30)
    search_entry.pack(side="left", padx=5)

    # Creating Table
    columns = ("id", "name", "product name", "date", "income", "job position", "credit score", "amount requested", "loan purpose", "status", "officer notes", "loan term")

    tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)

    tree.heading("id", text="ID")
    tree.heading("name", text="Customer Name")
    tree.heading("product name", text="Product Name")
    tree.heading("date", text="Application Date")
    tree.heading("income", text="Income £")
    tree.heading("job position", text="Job Position")
    tree.heading("credit score", text="Credit Score")
    tree.heading("amount requested", text="Amount Requested £")
    tree.heading("loan purpose", text="Loan Purpose")
    tree.heading("status", text="Status")
    tree.heading("officer notes", text="Officer Notes")
    tree.heading("loan term", text="Loan Term (months)")

    tree.column("id", width=25)
    tree.column("name", width=150)
    tree.column("product name", width=100)
    tree.column("date")
    tree.column("income", width=100)
    tree.column("job position", width=100)
    tree.column("credit score", width=100)
    tree.column("amount requested", width=100)
    tree.column("loan purpose", width=150)
    tree.column("status", width=100)
    tree.column("officer notes", width=150)
    tree.column("loan term", width=100)

    tree.pack(fill="both", expand=True, padx=15, pady=10)

    def load_applications():
        tree.delete(*tree.get_children())

        rows = application_service.get_all_applications()

        for row in rows:
            (application_id, customer_name, product_name, date, income, jobPosition, creditScore, amountRequested, loanPurpose, status, officerNotes, loanTermRequested, *_) = row

            item_id = tree.insert("", "end", values=(
                application_id, customer_name, product_name, date, income, jobPosition, creditScore, amountRequested, loanPurpose, status, officerNotes, loanTermRequested
            ))
    
    ## TODO - MAKE CUSTOMER AND PRODUCT DROPDOWN

    # Add and Save application to list
    def on_add_application():
        popup = tk.Toplevel(frame)
        popup.title("Add Application")
        popup.geometry("350x550")
        popup.transient(frame)
        popup.grab_set()

        tk.Label(popup, text="Customer Name").pack(pady=5)
        name_entry = tk.Entry(popup)
        name_entry.pack()

        tk.Label(popup, text="Product Name").pack(pady=5)
        product_entry = tk.Entry(popup)
        product_entry.pack()

        tk.Label(popup, text="Income £").pack(pady=5)
        income_entry = tk.Entry(popup)
        income_entry.pack()

        tk.Label(popup, text="Job Position").pack(pady=5)
        job_entry = tk.Entry(popup)
        job_entry.pack()

        tk.Label(popup, text="Credit Score").pack(pady=5)
        credit_entry = tk.Entry(popup)
        credit_entry.pack()

        tk.Label(popup, text="Amount Requested").pack(pady=5)
        amount_entry = tk.Entry(popup)
        amount_entry.pack()

        tk.Label(popup, text="Loan Purpose").pack(pady=5)
        purpose_entry = tk.Entry(popup)
        purpose_entry.pack()

        tk.Label(popup, text="Officer Notes").pack(pady=5)
        notes_entry = tk.Entry(popup)
        notes_entry.pack()

        tk.Label(popup, text="Term Requested").pack(pady=5)
        term_entry = tk.Entry(popup)
        term_entry.pack()

        def save_application():
            try:
                application_service.create_application(
                    name_entry.get(),
                    product_entry.get(),
                    income_entry.get(),
                    job_entry.get(),
                    credit_entry.get(),
                    amount_entry.get(),
                    purpose_entry.get(),
                    notes_entry.get(),
                    term_entry.get()
                )

                load_applications()
                popup.destroy()

            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(popup, text="Save", width=10, command=save_application).pack(pady=15)   

    def on_edit_application():

        selected = tree.selection()

        if not selected:
            messagebox.showwarning(
                title="No selection",
                message="Please select a application to delete"
            )
            return
        
        item_id = selected[0]
        values = tree.item(item_id, "values")

        application_id = values[0]

        popup = tk.Toplevel(frame)
        popup.title("Edit Application")
        popup.geometry("350x150")
        popup.transient(frame)
        popup.grab_set()

        # TODO - MAKE STATUS DROPDOWN ("Pending, "Approved", "Denied")
        status_var = tk.StringVar()

        status_combo = ttk.Combobox(
            popup,
            textvariable=status_var,
            values=["Pending", "Approved", "Denied"],
            state="readonly"
        )
        status_combo.pack(anchor="center", pady=50)
        status_combo.set(values[9])


        def save_changes():
            try:
                application_service.update_application(
                    application_id,
                    status_var.get(),   
                )

                tree.item(
                    item_id,
                    values=(
                        application_id,
                        status_var.get(),
                    )
                )
                load_applications()
                popup.destroy()

            except sqlite3.IntegrityError as e:
                messagebox.showerror("Approval denied, requests are putside scope of product", str(e))

                
            popup.destroy()

        tk.Button(popup, text="Save Changes", width=15, command=save_changes).pack(pady=15)

    def on_delete_application():

        selected = tree.selection()

        if not selected:
            messagebox.showwarning(
                title="No selection",
                message="Please select an application to delete"
            )
            return
        
        confirm = messagebox.askyesno(
        title="Confirm deletion",
        message="Are you sure you want to delete the selected application?"
    )
        if not confirm:
            return
        
        item_id = selected[0]
        application_id = tree.item(item_id,"values")[0]

        application_service.delete_application(application_id)
        tree.delete(item_id)

    tk.Button(toolbar, text="Add", width=10, command=on_add_application).pack(side="left", padx=5)
    tk.Button(toolbar, text="Edit", width=10, command=on_edit_application).pack(side="left", padx=5)
    tk.Button(toolbar, text="Delete", width=10, command=on_delete_application).pack(side="left", padx=5)


    spacer = tk.Frame(frame)
    spacer.pack(fill="both", expand=True)

     # Return flow
    def on_return_click():
        app_context["frames"]["main"].tkraise()
    
    tk.Button(frame, text="Return", width=15, command=on_return_click).pack(anchor="se", padx=15, pady=15)
    load_applications()