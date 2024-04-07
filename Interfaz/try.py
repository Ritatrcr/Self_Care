import tkinter as tk  # Importa la librería tkinter para la interfaz gráfica
from tkinter import PhotoImage  # Importa PhotoImage para trabajar con imágenes
import customtkinter  # Importa customtkinter, que parece ser una biblioteca personalizada
from customtkinter import CTkEntry, CTkButton  # Importa widgets personalizados de customtkinter
from tkcalendar import Calendar  # Importa el widget de calendario desde la biblioteca tkcalendar


class App(tk.Tk):
    def __init__(self):
        super().__init__()  # Inicializa la clase base de Tkinter
        self.geometry("340x200")  # Establece las dimensiones de la ventana
        self.imagen = PhotoImage(file="./Archivos/Background2.png")  # Carga una imagen

        self.label_imagen = tk.Label(self.master, image=self.imagen)  # Crea un widget Label con la imagen
        self.label_imagen.place(x=0, y=0, relwidth=1, relheight=1)  # Coloca la imagen en la ventana
        self.switch_to_start_page()  # Cambia a la página de inicio

    def switch_to_start_page(self):
        self.clear_frames()  # Limpia los frames existentes
        self.start_page = StartPage(self)  # Crea la página de inicio
        self.start_page.pack()  # Empaqueta la página de inicio en la ventana

    def switch_to_login_page(self):
        self.clear_frames()
        self.login_page = LogIn(self)
        self.login_page.pack()

    def switch_to_signup_page(self):
        self.clear_frames()
        self.signup_page = SignUp(self)
        self.signup_page.pack()

    def switch_to_main_page(self):
        self.clear_frames()
        self.main_page = MainPage(self)
        self.main_page.pack()

    def clear_frames(self):
        for widget in self.winfo_children():
            widget.pack_forget()  # Elimina todos los widgets empaquetados


class StartPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Start page")  # Establece el título de la página de inicio
        self.master.geometry("340x667")  # Establece las dimensiones de la ventana

        self.button_login = CTkButton(self, text="Log In",  # Crea un botón de inicio de sesión
                                      command=self.master.switch_to_login_page,
                                      fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.button_login.pack(pady=5)  # Empaqueta el botón en el frame

        self.button_signup = CTkButton(self, text="Sign Up",  # Crea un botón de registro
                                        command=self.master.switch_to_signup_page,
                                        fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.button_signup.pack(pady=5)  # Empaqueta el botón en el frame


class LogIn(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Log In")  # Establece el título de la página de inicio de sesión

        self.create_widgets()  # Crea los widgets en la página de inicio de sesión

        self.button_main_page = CTkButton(self, text="Log In",  # Crea un botón de inicio de sesión
                                          command=self.master.switch_to_main_page,
                                          fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.button_main_page.pack(pady=5)  # Empaqueta el botón en el frame

        self.button_back = CTkButton(self, text="Back to Start Page",  # Crea un botón para volver a la página de inicio
                                      command=self.master.switch_to_start_page,
                                      fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.button_back.pack(pady=5)  # Empaqueta el botón en el frame

    def create_widgets(self):
        # Crea etiquetas y campos de entrada para el nombre de usuario y la contraseña
        self.label_username = tk.Label(self, text="Username:")
        self.label_username.pack()
        self.entry_username = CTkEntry(self, placeholder_text="Username")
        self.entry_username.pack()

        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack()
        self.entry_password = CTkEntry(self, show="*", placeholder_text="Password")
        self.entry_password.pack()


class SignUp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.master.title("Sign Up")  # Establece el título de la página de registro

        self.button_main_page = CTkButton(self, text="Sign Up",  # Crea un botón de registro
                                          command=self.master.switch_to_main_page,
                                          fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.button_main_page.pack(pady=5)  # Empaqueta el botón en el frame

        self.button_back = CTkButton(self, text="Back to Start Page",  # Crea un botón para volver a la página de inicio
                                      command=self.master.switch_to_start_page,
                                      fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.button_back.pack(pady=5)  # Empaqueta el botón en el frame

    def create_widgets(self):
        # Crea etiquetas y campos de entrada para el nombre de usuario, la contraseña y el correo electrónico
        self.label_username = tk.Label(self, text="Username:")
        self.label_username.pack()
        self.entry_username = CTkEntry(self, placeholder_text="Username")
        self.entry_username.pack()

        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack()
        self.entry_password = CTkEntry(self, show="*", placeholder_text="Password")
        self.entry_password.pack()

        self.label_email = tk.Label(self, text="Email:")
        self.label_email.pack()
        self.entry_email = CTkEntry(self, placeholder_text="Email")
        self.entry_email.pack()


class MainPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Main Page")  # Establece el título de la página principal
        self.initial_stage()  # Inicializa la etapa inicial de la página principal

    def switch_to_initial_stage(self):
        self.master.clear_frames()  # Limpia los frames existentes
        self.initial_stage()  # Inicializa la etapa inicial de la página principal
        self.pack()  # Empaqueta la página principal en la ventana

    def initial_stage(self):
        # Crea los widgets en la página principal
        label = tk.Label(self, text="Main Page", font=("Helvetica", 16))
        label.pack(pady=10)

        # Crea botones para acceder a diferentes secciones
        self.button_about_us = CTkButton(self, text="About Us", command=self.about_us)
        self.button_about_us.pack(pady=5)

        self.button_calendar = CTkButton(self, text="Calendar", command=self.calendar)
        self.button_calendar.pack(pady=5)

        self.button_feelings = CTkButton(self, text="Feelings", command=self.feelings)
        self.button_feelings.pack(pady=5)

        self.button_sleep = CTkButton(self, text="Sleep", command=self.sleep)
        self.button_sleep.pack(pady=5)

        # Crea un botón para cerrar sesión
        button_logout = CTkButton(self, text="Log Out", command=self.master.switch_to_start_page,
                                  fg_color="pink", text_color="black")
        button_logout.pack(pady=5)

    def back_to_main_page(self):
        # Agrega un botón para volver a la página principal
        back_button = CTkButton(self.master, text="Back to Main Page", command=self.master.switch_to_main_page)
        back_button.pack(pady=10)

    def about_us(self):
        # Limpia los frames existentes y establece el título
        self.master.clear_frames()
        self.master.title("About Us")

        # Agrega el texto al frame principal
        about_text = """
        This is the About Us page.
        Welcome to our application!
        We hope you find it useful.
        """
        about_label = tk.Label(self.master, text=about_text, justify="left")
        about_label.pack(pady=10)

        # Agrega un botón para volver a la página principal
        self.back_to_main_page()

    def calendar(self):
        # Limpia los frames y establece el título
        self.master.clear_frames()
        self.master.title("Calendar")

        # Crea y muestra el widget de calendario
        calendar = Calendar(self.master, selectmode='day')
        calendar.pack(pady=10)

        self.back_to_main_page()

    def feelings(self):
        # Limpia los frames y establece el título
        self.master.clear_frames()
        self.master.title("Focus")

        # Agrega la etiqueta "¿Cómo te sientes hoy?"
        label_text = "¿Cómo te sientes hoy?"
        label = tk.Label(self.master, text=label_text, font=("Helvetica", 16))
        label.pack(pady=10)

        # Agrega botones para representar emociones
        button_happy = CTkButton(self.master, text="😊 Happy")
        button_happy.pack(pady=5)

        button_sad = CTkButton(self.master, text="😢 Sad")
        button_sad.pack(pady=5)

        button_angry = CTkButton(self.master, text="😠 Angry")
        button_angry.pack(pady=5)

        self.back_to_main_page()

    def sleep(self):
        # Limpia los frames y establece el título
        self.master.clear_frames()
        self.master.title("Sleep")

        sleep_info = """
        Quality sleep is crucial for health and well-being.
        """
        label = tk.Label(self.master, text=sleep_info, font=("Helvetica", 12), justify="left", wraplength=400)
        label.pack(pady=10)

        self.back_to_main_page()


if __name__ == "__main__":
    app = App()
    app.mainloop()  # Inicia el bucle principal del programa
