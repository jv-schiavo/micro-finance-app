import tkinter as tk

from ui.login_view import build_login_view
from ui.main_menu_view import build_main_menu_view
from db.connection import get_connection
from ui.product_view import build_products_view
from ui.repayment_view import build_repayments_view
from ui.application_view import build_applications_view
from ui.report_view import build_reports_view
from ui.customer_view import build_customers_view

def main():
    root = tk.Tk()
    root.title("Micro Finance Management System")
    root.geometry("1000x800")

    
    # db connection
    conn = get_connection()

    # Main container
    container = tk.Frame(root)
    container.grid(row=0, column=0, sticky="nsew")

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    container.rowconfigure(0, weight=1)
    container.columnconfigure(0, weight=1)

    # Shared app state
    frames = {}
    app_context = {
        "db": conn,
        "frames": frames
    }

    # Build screens
    build_login_view(container, app_context )
    build_main_menu_view(container, app_context)
    build_products_view(container, app_context)
    build_repayments_view(container, app_context)
    build_applications_view(container, app_context)
    build_reports_view(container, app_context)
    build_customers_view(container, app_context)

    # Show login first
    frames["login"].tkraise()

    root.mainloop()

if __name__ == "__main__":
    main()    






