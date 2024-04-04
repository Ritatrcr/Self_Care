import tkinter as tk
from tkinter import PhotoImage

#Crea clase
class SignInWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Sign In")
        self.master.geometry("340x667")  # width x height, in pixels

        self.create_widgets()

    def create_widgets(self):
        # Etiquetas y campos de entrada para nombre de usuario y contraseña
        self.label_username = tk.Label(self.master, text="Username:")
        self.label_username.pack()
        self.entry_username = tk.Entry(self.master)
        self.entry_username.pack()

        self.label_password = tk.Label(self.master, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self.master, show="*")  # Mostrar asteriscos en lugar de texto
        self.entry_password.pack()

        self.label_email = tk.Label(self.master, text="Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(self.master)
        self.entry_email.pack()

        # Botón de inicio de sesión
        self.button_login = tk.Button(self.master, text="Sign In", command=self.login)
        self.button_login.pack(pady=10)

    def login(self):
        # Método que maneja el evento de inicio de sesión
        username = self.entry_username.get()
        password = self.entry_password.get()
        email = self.entry_email.get()

        # Aquí puedes implementar la lógica de autenticación
        print("Username:", username)
        print("Password:", password)