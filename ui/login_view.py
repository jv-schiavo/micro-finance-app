import tkinter as tk

def build_login_view(parent, app_context):
    frame = tk.Frame(parent)
    app_context["frames"]["login"] = frame
    frame.grid(row=0, column=0, sticky="nsew")
    
    content = tk.Frame(frame)
    content.place(relx=0.5, rely=0.5, anchor="center")
   
    tk.Label(content, text="Login", font=("Arial", 18, "bold")).pack(pady=10)

    tk.Label(content, text="Username").pack()
    tk.Entry(content).pack()

    tk.Label(content, text="Password").pack()
    tk.Entry(content, show="*").pack()

    def on_login_click():
        # No auth yet. Just prove navigation works.
        app_context["frames"]["main"].tkraise()

    tk.Button(content, text="Login", width=15, command=on_login_click).pack(pady=10)

    


