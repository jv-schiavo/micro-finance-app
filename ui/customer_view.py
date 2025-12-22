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

    toolbar = tk.Frame(frame)
    toolbar.pack(anchor="w", padx=15, pady=5)

    search_frame = tk.Frame(frame)
    search_frame.pack(anchor="w", padx=15, pady=5)
    tk.Label(search_frame, text="Search:").pack(side="left")
    search_entry = tk.Entry(search_frame, width=30)
    search_entry.pack(side="left", padx=5)

    # Creating Table
    columns = ("id", "name", "DOB", "address", "phone", "nationalID")

    tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)

    tree.heading("id", text="ID")
    tree.heading("name", text="Customer Name")
    tree.heading("DOB", text="Date of Birth")
    tree.heading("address", text="Address")
    tree.heading("phone", text="Phone Number")
    tree.heading("nationalID", text="National ID")

    tree.column("id", width=50, anchor="center")
    tree.column("name", width=220)
    tree.column("DOB", width=100, anchor="center")
    tree.column("address", width=200)
    tree.column("phone", width=100)
    tree.column("nationalID", width=100, anchor="center")

    tree.pack(fill="both", expand=True, padx=15, pady=10)

    # Add and Save application to list
    def on_add_customer():
        popup = tk.Toplevel(frame)
        popup.title("Add Customer")
        popup.geometry("350x450")
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

        tk.Label(popup, text="National ID").pack(pady=5)
        national_entry = tk.Entry(popup)
        national_entry.pack()

        image_bytes = None
        def upload_image():
            nonlocal image_bytes

            file_path = filedialog.askopenfilename(
                filetypes=[("Image files", "*.png *.jpg *.jpeg")]
            )
            if not file_path:
                return

            img = Image.open(file_path)
            img.thumbnail((200, 200))

            photo = ImageTk.PhotoImage(img)
            image_label.config(image=photo)
            image_label.image = photo

            with open(file_path, "rb") as f:
                image_bytes = f.read()

        tk.Label(popup, text="National ID Photo").pack(pady=5)

        image_label = tk.Label(popup, width=200, height=200, relief="solid")
        image_label.pack(pady=5)

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


    spacer = tk.Frame(frame)
    spacer.pack(fill="both", expand=True)

    preview_panel = tk.Frame(frame)
    preview_panel.pack(side="right", padx=15, pady=15)

    tk.Label(preview_panel, text="National ID Preview").pack()

    id_preview = tk.Label(
        preview_panel,
        width=300,
        height=300,
        relief="solid"
    )
    id_preview.pack()

    def on_customer_select(event):
        selected = tree.selection()
        if not selected:
            id_preview.config(image="")
            id_preview.image = None
            return

        item_id = selected[0]

        image_bytes = customer_images.get(item_id)
        if not image_bytes:
            id_preview.config(image="")
            return

        img = Image.open(io.BytesIO(image_bytes))
        img.thumbnail((300, 300))

        photo = ImageTk.PhotoImage(img)
        id_preview.config(image=photo)
        id_preview.image = photo

    tree.bind("<<TreeviewSelect>>", on_customer_select)


     # Return flow
    def on_return_click():
        app_context["frames"]["main"].tkraise()
    
    tk.Button(frame, text="Return", width=15, command=on_return_click).pack(anchor="se", padx=15, pady=15)