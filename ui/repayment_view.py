import tkinter as tk

def build_repayments_view(parent, app_context):
    frame = tk.Frame(parent)
    app_context["frames"]["repayments"] = frame

    frame.grid(row=0, column=0, sticky="nsew")

    tk.Label(frame, text="Repayments", font=("Arial", 18, "bold")).pack()

    spacer = tk.Frame(frame)
    spacer.pack(fill="both", expand=True)

     # Return flow
    def on_return_click():
        app_context["frames"]["main"].tkraise()
    
    tk.Button(frame, text="Return", width=15, command=on_return_click).pack(anchor="se", padx=15, pady=15)
