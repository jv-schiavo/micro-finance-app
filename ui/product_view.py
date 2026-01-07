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
    columns = ("id", "name", "rate", "minAmount", "maxAmount", "fees", "minTerm", "maxTerm")

    tree = ttk.Treeview(frame, columns=columns, show="headings")

    tree.heading("id", text="ID")
    tree.heading("name", text="Product Name")
    tree.heading("rate", text="Interest Rate %")
    tree.heading("minAmount", text="Minimum Amount")
    tree.heading("maxAmount", text="Maximum Amount")
    tree.heading("fees", text="Fees £")
    tree.heading("minTerm", text="Minimum Term")
    tree.heading("maxTerm", text="Maximum Term")

    tree.column("id", width=50)
    tree.column("name", width=180)
    tree.column("rate", width=100)
    tree.column("minAmount", width=100)
    tree.column("maxAmount", width=100)
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
            name = name_entry.get()
            rate = rate_entry.get()
            minAmout = minAmount_entry.get()
            maxAmount = maxAmount_entry.get()
            fees = fees_entry.get()
            minTerm = minTerm_entry.get()
            maxTerm = maxTerm_entry.get()

            

            if not (name and rate and minAmout and maxAmount and fees and minTerm and maxTerm):
                return
            
            tree.insert("","end",values=("", name, rate, minAmout, maxAmount, fees, minTerm, maxTerm))
            print("SAVED")
            popup.destroy()

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
        
        for item in selected:
            tree.delete(item)

    def on_edit_product():

        selected = tree.selection()

        if not selected:
            messagebox.showwarning(
                title="No selection",
                message="Please select a product to delete"
            )
            return
        
        item_id = selected[0]
        values = tree.item(item_id, "values")

        popup = tk.Toplevel(frame)
        popup.title("Edit Product")
        popup.geometry("350x450")
        popup.transient(frame)
        popup.grab_set()

        def labeled_entry(label, value):
            tk.Label(popup, text=label).pack(pady=3)
            e = tk.Entry(popup)
            e.insert(0, value)
            e.pack()
            return e

        name_entry = labeled_entry("Product Name", values[1])
        rate_entry = labeled_entry("Interest Rate %", values[2])
        minAmount_entry = labeled_entry("Minimum Amount", values[3])
        maxAmount_entry = labeled_entry("Maximum Amount", values[4])
        fees_entry = labeled_entry("Fees", values[5])
        minTerm_entry = labeled_entry("Minimum Term", values[6])
        maxTerm_entry = labeled_entry("Maximum Term", values[7])

        def save_changes():
            tree.item(
                item_id,
                values=(
                    values[0],
                    name_entry.get(),
                    rate_entry.get(),
                    minAmount_entry.get(),
                    maxAmount_entry.get(),
                    fees_entry.get(),
                    minTerm_entry.get(),
                    maxTerm_entry.get()
                )
            )
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