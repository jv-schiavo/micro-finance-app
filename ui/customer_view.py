import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import io


def build_customers_view(parent, app_context):
    customer_images = {}

    frame = tk.Frame(parent)
    app_context["frames"]["customers"] = frame
    frame.grid(row=0, column=0, sticky="nsew")

    # Title
    tk.Label(frame, text="Customers", font=("Arial", 18, "bold")).pack(anchor="w", padx=15, pady=(10,5))

    # Toolbar
    toolbar = tk.Frame(frame)
    toolbar.pack(anchor="w", padx=15, pady=5)

    search_frame = tk.Frame(frame)
    search_frame.pack(anchor="w", padx=15, pady=5)
    tk.Label(search_frame, text="Search:").pack(side="left")
    tk.Entry(search_frame, width=30).pack(side="left", padx=5)

    # Content
    content = tk.Frame(frame)
    content.pack(fill="both", expand=True, padx=15, pady=10)

    content.grid_columnconfigure(0, weight=4) # Table
    content.grid_columnconfigure(1, weight=1) # preview
    content.grid_rowconfigure(0, weight=1)

    # Creating Table
    table_container = tk.Frame(content)
    table_container.pack(side="left", fill="both", expand=True)

    columns = ("id", "name", "dob", "address", "phone", "nationalID")
    tree = ttk.Treeview(table_container, columns=columns, show="headings")

    tree.heading("id", text="ID")
    tree.heading("name", text="Customer Name")
    tree.heading("dob", text="Date of Birth")
    tree.heading("address", text="Address")
    tree.heading("phone", text="Phone Number")
    tree.heading("nationalID", text="National ID")

    tree.column("id", width=50, anchor="center")
    tree.column("name", width=220)
    tree.column("dob", width=110, anchor="center")
    tree.column("address", width=200)
    tree.column("phone", width=120)
    tree.column("nationalID", width=120)

    tree.pack(fill="both", expand=True)

    # Photo Preview
    preview_panel = tk.Frame(content, width=300, height=220, relief="groove", bd=2)
    preview_panel.pack(side="right", fill="y", padx=(15, 0))
    preview_panel.grid_propagate(False)

    tk.Label(preview_panel,
              text="ID Photo", 
              font=("Arial", 11, "bold")
    ).pack(pady=8)          

    id_preview = tk.Label(
        preview_panel,
        width=260,
        height=140,
        relief="solid",
        text="Select a customer",
        justify="center"
    )
    id_preview.pack(pady=10)

    def on_customer_select(event):
        selected = tree.selection()
        if not selected:
            id_preview.config(image="", text="Select a customer")
            id_preview.image = None
            return
        
        image_bytes = customer_images.get(selected[0])
        if not image_bytes:
            id_preview.config(text="No image")
            return
        
        img = Image.open(io.BytesIO(image_bytes))
        img.thumbnail((260, 140))
        photo = ImageTk.PhotoImage(img)

        id_preview.config(image=photo, text="")
        id_preview.image = photo

    tree.bind("<<TreeviewSelect>>", on_customer_select)

    
    # Add and Save application to list
    def on_add_customer():
        popup = tk.Toplevel(frame)
        popup.title("Add Customer")
        popup.geometry("350x600")
        popup.transient(frame)
        popup.grab_set()

        tk.Label(popup, text="Customer Name").pack(pady=5)
        name_entry = tk.Entry(popup)
        name_entry.pack()

        tk.Label(popup, text="DOB").pack(pady=5)
        dob_entry = tk.Entry(popup)
        dob_entry.pack()

        tk.Label(popup, text="Address").pack(pady=5)
        address_entry = tk.Entry(popup)
        address_entry.pack()

        tk.Label(popup, text="Phone Number").pack(pady=5)
        phone_entry = tk.Entry(popup)
        phone_entry.pack()

        tk.Label(popup,text="National ID").pack(pady=5)
        national_entry = tk.Entry(popup)
        national_entry.pack()

        image_bytes = None

        photo_frame = tk.Frame(popup, width=240, height=140)
        photo_frame.pack(pady=10)
        photo_frame.pack_propagate(False)

        tk.Label(photo_frame, text="National ID Photo").pack(anchor="w")

        photo_preview = tk.Label(
            photo_frame,
            relief="solid",
            text="No image selected",
            justify="center"
        )
        photo_preview.pack(fill="both", expand=True)

        def upload_image():
            nonlocal image_bytes

            file_path = filedialog.askopenfilename(
                filetypes=[("Image files", "*.png *.jpg *.jpeg")]
            )
            if not file_path:
                return

            img = Image.open(file_path)
            img.thumbnail((220, 120))

            photo = ImageTk.PhotoImage(img)
            photo_preview.config(image=photo, text="")
            photo_preview.image = photo
            
            with open(file_path, "rb") as f:
                image_bytes = f.read()

        tk.Button(popup, text="Upload Image", command=upload_image).pack(pady=5)

        def save_customer():
            name = name_entry.get()
            dob = dob_entry.get()
            address = address_entry.get()
            phone = phone_entry.get()
            national = national_entry.get()

            if not (name and dob and address and phone and national):
                messagebox.showwarning("Missing data", "All fields are required.")
                return

            if not image_bytes:
                messagebox.showwarning(
                    "Missing document",
                    "National ID photo is required."
                )
                return

            item_id = tree.insert(
                "",
                "end",
                values=("", name, dob, address, phone, national)
            )
            print("Saved")
            customer_images[item_id] = image_bytes
            popup.destroy()


        tk.Button(popup, text="Save", width=10, command=save_customer).pack(pady=15)   

    def on_edit_customer():

        selected = tree.selection()

        if not selected:
            messagebox.showwarning(
                title="No selection",
                message="Please select a customer to edit"
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

        name_entry = labeled_entry("Customer Name", values[1])
        address_entry = labeled_entry("Address", values[3])
        phone_entry = labeled_entry("Phone Number", values[4])

        def save_changes():
            tree.item(
                item_id,
                values=(
                    values[0],
                    name_entry.get(),
                    values[2],
                    address_entry.get(),
                    phone_entry.get(),
                    values[5]
                )
            )
            popup.destroy()

        tk.Button(popup, text="Save Changes", width=15, command=save_changes).pack(pady=15)

    def on_delete_customer():

        selected = tree.selection()

        if not selected:
            messagebox.showwarning(
                title="No selection",
                message="Please select a customer to delete"
            )
            return
        
        confirm = messagebox.askyesno(
        title="Confirm deletion",
        message="Are you sure you want to delete the selected customer?"
    )
        if not confirm:
            return
        
        for item in selected:
            customer_images.pop(item, None)
            tree.delete(item)

        id_preview.config(image="")
        id_preview.image = None      

    tk.Button(toolbar, text="Add", width=10, command=on_add_customer).pack(side="left", padx=5)
    tk.Button(toolbar, text="Edit", width=10, command=on_edit_customer).pack(side="left", padx=5)
    tk.Button(toolbar, text="Delete", width=10, command=on_delete_customer).pack(side="left", padx=5)

     # Return flow
    def on_return_click():
        app_context["frames"]["main"].tkraise()
    
    tk.Button(toolbar, text="Return", width=10, command=on_return_click).pack(side="right")