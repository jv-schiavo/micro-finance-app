import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



def build_products_view(parent, app_context):
    frame = tk.Frame(parent)
    app_context["frames"]["products"] = frame
    frame.grid(row=0, column=0, sticky="nsew")

    product_service = app_context["services"]["product"]

    # Title
    tk.Label(frame, text="Product Management", font=("Arial", 18, "bold")).pack(anchor="w", padx=15, pady=(10,5))

    toolbar = tk.Frame(frame)
    toolbar.pack(anchor="w", padx=15, pady=5)

    search_frame = tk.Frame(frame)
    search_frame.pack(anchor="w", padx=15, pady=5)

    tk.Label(search_frame, text="Search:").pack(side="left")
    search_entry = tk.Entry(search_frame, width=30)
    search_entry.pack(side="left", padx=5)

    # Creating Table
    columns = ("id", "name", "rate", "minAmount", "maxAmount", "termRange", "fees", "minTerm", "maxTerm")

    tree = ttk.Treeview(frame, columns=columns, show="headings")

    tree.heading("id", text="ID")
    tree.heading("name", text="Product Name")
    tree.heading("rate", text="Interest Rate %")
    tree.heading("minAmount", text="Minimum Amount")
    tree.heading("maxAmount", text="Maximum Amount")
    tree.heading("termRange", text="Loan Term Range")
    tree.heading("fees", text="Fees £")
    tree.heading("minTerm", text="Minimum Term")
    tree.heading("maxTerm", text="Maximum Term")

    tree.column("id", width=50)
    tree.column("name", width=180)
    tree.column("rate", width=100)
    tree.column("minAmount", width=100)
    tree.column("maxAmount", width=100)
    tree.column("termRange", width=80)
    tree.column("fees", width=100)
    tree.column("minTerm", width=100)
    tree.column("maxTerm", width=100)

    tree.pack(fill="both", expand=True, padx=15, pady=10)

    # Load all products
    def load_products():
        tree.delete(*tree.get_children())
        for row in product_service.get_all_products():
            tree.insert("", "end", values=(
                row["product_id"],
                row["product_name"],
                row["interestRate"],
                row["minAmount"],
                row["maxAmount"],
                row["loanTermRange"],
                row["fees"],
                row["minLoanTermMonths"],
                row["maxLoanTermMonths"]

            ))
   
    # Add and Save product to list
    def on_add_product():
        popup = tk.Toplevel(frame)
        popup.title("Add Product")
        popup.geometry("350x450")
        popup.transient(frame)
        popup.grab_set()

        tk.Label(popup, text="Product Name").pack(pady=5)
        name_entry = tk.Entry(popup)
        name_entry.pack()

        tk.Label(popup, text="Interest Rate %").pack(pady=5)
        rate_entry = tk.Entry(popup)
        rate_entry.pack()

        tk.Label(popup, text="Minimum Amount").pack(pady=5)
        minAmount_entry = tk.Entry(popup)
        minAmount_entry.pack()

        tk.Label(popup, text="Maximum Amount").pack(pady=5)
        maxAmount_entry = tk.Entry(popup)
        maxAmount_entry.pack()

        tk.Label(popup, text="Loan Term Range").pack(pady=5)
        termRange_entry = tk.Entry(popup)
        termRange_entry.pack()

        tk.Label(popup, text="Fees").pack(pady=5)
        fees_entry = tk.Entry(popup)
        fees_entry.pack()

        tk.Label(popup, text="Minimum Term").pack(pady=5)
        minTerm_entry = tk.Entry(popup)
        minTerm_entry.pack()

        tk.Label(popup, text="Maximum Term").pack(pady=5)
        maxTerm_entry = tk.Entry(popup)
        maxTerm_entry.pack()

        def save_product():
            try:
                product_service.create_product(
                    name_entry.get(),
                    float(rate_entry.get()),
                    float(minAmount_entry.get()),
                    float(maxAmount_entry.get()),
                    termRange_entry.get(),
                    float(fees_entry.get()),
                    minTerm_entry.get(),
                    maxTerm_entry.get()
                )
                load_products()
                popup.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))


        tk.Button(popup, text="Save", width=10, command=save_product).pack(pady=15)

    def on_delete_product():

        selected = tree.selection()

        if not selected:
            messagebox.showwarning(
                title="No selection",
                message="Please select a product to delete"
            )
            return
        
        confirm = messagebox.askyesno(
        title="Confirm deletion",
        message="Are you sure you want to delete the selected product?"
    )

        if not confirm:
            return
        
        item_id = selected[0]
        product_id = tree.item(item_id, "values")[0]  # PK column

        product_service.delete_product(product_id)
        tree.delete(item_id)

    def on_edit_product():

        selected = tree.selection()

        if not selected:
            messagebox.showwarning(
                title="No selection",
                message="Please select a product to edit"
            )
            return
        
        item_id = selected[0]
        values = tree.item(item_id, "values")

        product_id = values[0]  


        popup = tk.Toplevel(frame)
        popup.title("Edit Product")
        popup.geometry("350x450")
        popup.transient(frame)
        popup.grab_set()

        tk.Label(popup, text="Product Name").pack(pady=5)
        name_entry = tk.Entry(popup)
        name_entry.insert(0, values[1])
        name_entry.pack()

        tk.Label(popup, text="Interest Rate %").pack(pady=5)
        rate_entry = tk.Entry(popup)
        rate_entry.insert(0, values[2])
        rate_entry.pack()

        tk.Label(popup, text="Minimum Amount").pack(pady=5)
        minAmount_entry = tk.Entry(popup)
        minAmount_entry.insert(0, values[3])
        minAmount_entry.pack()

        tk.Label(popup, text="Maximum Amount").pack(pady=5)
        maxAmount_entry = tk.Entry(popup)
        maxAmount_entry.insert(0, values[4])
        maxAmount_entry.pack()

        tk.Label(popup, text="Loan Term Range").pack(pady=5)
        termRange_entry = tk.Entry(popup)
        termRange_entry.insert(0, values[5])
        termRange_entry.pack()

        tk.Label(popup, text="Fees").pack(pady=5)
        fees_entry = tk.Entry(popup)
        fees_entry.insert(0, values[6])
        fees_entry.pack()

        tk.Label(popup, text="Minimum Term").pack(pady=5)
        minTerm_entry = tk.Entry(popup)
        minTerm_entry.insert(0, values[7])
        minTerm_entry.pack()

        tk.Label(popup, text="Maximum Term").pack(pady=5)
        maxTerm_entry = tk.Entry(popup)
        maxTerm_entry.insert(0, values[8])
        maxTerm_entry.pack()


        def save_changes():
            product_service.update_product(
                    product_id,
                    name_entry.get(),
                    rate_entry.get(),
                    minAmount_entry.get(),
                    maxAmount_entry.get(),
                    termRange_entry.get(),
                    fees_entry.get(),
                    minTerm_entry.get(),
                    maxTerm_entry.get()
                )
           

            tree.item(item_id, values=(
                product_id,
                name_entry.get(),
                rate_entry.get(),
                minAmount_entry.get(),
                maxAmount_entry.get(),
                termRange_entry.get(),
                fees_entry.get(),
                minTerm_entry.get(),
                maxTerm_entry.get()

            ))

            popup.destroy()

        tk.Button(popup, text="Save Changes", width=15, command=save_changes).pack(pady=15)

    
    tk.Button(toolbar, text="Add", width=10, command=on_add_product).pack(side="left", padx=5)
    tk.Button(toolbar, text="Delete", width=10, command=on_delete_product).pack(side="left", padx=5)
    tk.Button(toolbar, text="Edit", width=10, command=on_edit_product).pack(side="left", padx=5)
    
                
    

    spacer = tk.Frame(frame)
    spacer.pack(fill="both", expand=True)

    # Return flow
    def on_return_click():
        app_context["frames"]["main"].tkraise()
    
    tk.Button(frame, text="Return", width=15, command=on_return_click).pack(anchor="se", padx=15, pady=15)

    load_products()