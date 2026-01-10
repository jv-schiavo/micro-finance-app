import tkinter as tk

def build_loan_view(parent, app_context):
    frame = tk.Frame(parent)
    app_context["frames"]["loans"] = frame
    frame.grid(row=0, column=0, sticky="nsew")
    
    content = tk.Frame(frame)
    content.place(relx=0.5, rely=0.5, anchor="center")
   
    tk.Label(content, text="Loans", font=("Arial", 18, "bold")).pack(pady=10)


    def on_return_click():
        # No auth yet. Just prove navigation works.
        app_context["frames"]["main"].tkraise()

    tk.Button(content, text="Return", width=15, command=on_return_click).pack(pady=10)

    


