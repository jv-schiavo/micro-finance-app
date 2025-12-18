import tkinter as tk

def build_products_view(parent, app_context):
    frame = tk.Frame(parent)
    app_context["frames"]["products"] = frame
    frame.grid(row=0, column=0, sticky="nsew")

    # Title
    tk.Label(frame, text="Products", font=("Arial", 18, "bold")).pack()

    # Form
    form = tk.Frame(frame)
    form.pack(pady=10)

    tk.Label(form, text="Product Name").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    name_entry = tk.Entry(form, width=25)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form, text="Interest Rate %").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    rate_entry = tk.Entry(form, width=25)
    rate_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(form, text="Minimum Amount £").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    min_entry = tk.Entry(form, width=25)
    min_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(form, text="Maximum Amount £").grid(row=3, column=0, sticky="e", padx=5, pady=5)
    max_entry = tk.Entry(form, width=25)
    max_entry.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(form, text="Fees £").grid(row=4, column=0, sticky="e", padx=5, pady=5)
    fees_entry = tk.Entry(form, width=25)
    fees_entry.grid(row=2, column=4, padx=5, pady=5)

    tk.Label(form, text="Minimum Term (months)").grid(row=5, column=0, sticky="e", padx=5, pady=5)
    minTerm_entry = tk.Entry(form, width=25)
    minTerm_entry.grid(row=5, column=1, padx=5, pady=5)

    tk.Label(form, text="Maximum Term (months)").grid(row=6, column=0, sticky="e", padx=5, pady=5)
    maxTerm_entry = tk.Entry(form, width=25)
    maxTerm_entry.grid(row=6, column=1, padx=5, pady=5)


    spacer = tk.Frame(frame)
    spacer.pack(fill="both", expand=True)

    # Return flow
    def on_return_click():
        app_context["frames"]["main"].tkraise()
    
    tk.Button(frame, text="Return", width=15, command=on_return_click).pack(anchor="se", padx=15, pady=15)