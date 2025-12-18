import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def build_products_view(parent, app_context):
    frame = tk.Frame(parent)
    app_context["frames"]["products"] = frame
    frame.grid(row=0, column=0, sticky="nsew")

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

    tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)

    tree.heading("id", text="ID")
    tree.heading("name", text="Product Name")
    tree.heading("rate", text="Interest Rate %")
    tree.heading("minAmount", text="Minimum Amount")
    tree.heading("maxAmount", text="Maximum Amount")
    tree.heading("fees", text="Fees £")
    tree.heading("minTerm", text="Minimum Term")
    tree.heading("maxTerm", text="Maximum Term")

    tree.column("id", width=50, anchor="center")
    tree.column("name", width=180)
    tree.column("rate", width=100, anchor="center")
    tree.column("minAmount", width=100, anchor="center")
    tree.column("maxAmount", width=100, anchor="center")
    tree.column("fees", width=100, anchor="center")
    tree.column("minTerm", width=100, anchor="center")
    tree.column("maxTerm", width=100, anchor="center")

    tree.pack(fill="both", expand=True, padx=15, pady=10)

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

    def on_delet_product():
        selected = tree.selection()

        if not selected:
            messagebox.showwarning(
                title="No selection",
                message="Please select a product to delete"
            )
            return
        
        for item in selected:
            tree.delete(item)
        
    
    tk.Button(toolbar, text="Add", width=10, command=on_add_product).pack(side="left", padx=5)
    tk.Button(toolbar, text="Delete", width=10, command=on_delet_product).pack(side="left", padx=5)
    tk.Button(toolbar, text="Edit", width=10).pack(side="left", padx=5)
    
                
    

    spacer = tk.Frame(frame)
    spacer.pack(fill="both", expand=True)

    # Return flow
    def on_return_click():
        app_context["frames"]["main"].tkraise()
    
    tk.Button(frame, text="Return", width=15, command=on_return_click).pack(anchor="se", padx=15, pady=15)