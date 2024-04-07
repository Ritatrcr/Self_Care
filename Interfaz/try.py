import tkinter as tk
from tkinter import PhotoImage
import customtkinter
from customtkinter import CTkEntry, CTkButton  # Importa los widgets personalizados
from tkcalendar import Calendar  # Importa el widget de calendario


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("340x200")  # width x height, in pixels
        self.imagen = PhotoImage(file="./Archivos/Background2.png")

        self.label_imagen = tk.Label(self.master, image=self.imagen)
        self.label_imagen.place(x=0, y=0, relwidth=1, relheight=1)
        self.switch_to_start_page()
        

    def switch_to_start_page(self):
        self.clear_frames()
        self.start_page = StartPage(self)
        self.start_page.pack()

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
            widget.pack_forget()


class StartPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Start page")
        self.master.geometry("340x667")  # width x height, in pixels

        self.button_login = CTkButton(self, text="Log In",
                                      command=self.master.switch_to_login_page,
                                      fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.button_login.pack(pady=5)

        self.button_signup = CTkButton(self, text="Sign Up",
                                        command=self.master.switch_to_signup_page,
                                        fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))

        self.button_signup.pack(pady=5)

#side bar con log in y log out

class LogIn(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Log In")

        self.create_widgets()

        self.button_main_page = CTkButton(self, text="Log In",
                                          command=self.master.switch_to_main_page,
                                          fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.button_main_page.pack(pady=5)

        self.button_back = CTkButton(self, text="Back to Start Page",
                                      command=self.master.switch_to_start_page,
                                      fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.button_back.pack(pady=5)

    def create_widgets(self):
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
        self.master.title("Sign Up")

        self.button_main_page = CTkButton(self, text="Sign Up",
                                          command=self.master.switch_to_main_page,
                                          fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.button_main_page.pack(pady=5)

        self.button_back = CTkButton(self, text="Back to Start Page",
                                      command=self.master.switch_to_start_page,
                                      fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.button_back.pack(pady=5)

    def create_widgets(self):
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
        self.master.title("Main Page")  # Establece el título de la ventana
        self.initial_stage()

    def switch_to_initial_stage(self):
        self.master.clear_frames()
        self.initial_stage()
        self.pack()

    def initial_stage(self):
        # Crea los widgets en la página principal
        label = tk.Label(self, text="Main Page", font=("Helvetica", 16))
        label.pack(pady=10)

        self.button_about_us = CTkButton(self, text="About Us", command=self.about_us)
        self.button_about_us.pack(pady=5)

        self.button_calendar = CTkButton(self, text="Calendar", command=self.calendar)
        self.button_calendar.pack(pady=5)

        self.button_feelings = CTkButton(self, text="Feelings", command=self.feelings)
        self.button_feelings.pack(pady=5)

        self.button_sleep = CTkButton(self, text="Sleep", command=self.sleep)
        self.button_sleep.pack(pady=5)
        button_logout = CTkButton(self, text="Log Out", command=self.master.switch_to_start_page, fg_color="pink", text_color="black")
        button_logout.pack(pady=5)

    def back_to_main_page(self):
        # Add a button to go back to the main page
        back_button = CTkButton(self.master, text="Back to Main Page", command=self.master.switch_to_main_page)
        back_button.pack(pady=10)

    def about_us(self):
        # Clear any existing frames and set the title
        self.master.clear_frames()
        self.master.title("About Us")

        # Add the text to the main frame
        about_text = """
        This is the About Us page.
        Welcome to our application!
        We hope you find it useful.
        """
        about_label = tk.Label(self.master, text=about_text, justify="left")
        about_label.pack(pady=10)

        # Add a button to go back to the main page
        self.back_to_main_page()
        
    def calendar(self):
        # Clear frames and set the title
        self.master.clear_frames()
        self.master.title("Calendar")

        # Create and display the calendar widget
        calendar = Calendar(self.master, selectmode='day')
        calendar.pack(pady=10)

        self.back_to_main_page()


    def feelings(self):
        # Clear frames and set the title
        self.master.clear_frames()
        self.master.title("Focus")

        # Add the label "¿Cómo te sientes hoy?"
        label_text = "¿Cómo te sientes hoy?"
        label = tk.Label(self.master, text=label_text, font=("Helvetica", 16))
        label.pack(pady=10)

        # Add buttons to represent emotions
        button_happy = CTkButton(self.master, text="😊 Feliz")
        button_happy.pack(pady=5)

        button_sad = CTkButton(self.master, text="😢 Triste")
        button_sad.pack(pady=5)

        button_angry = CTkButton(self.master, text="😠 Enojado")
        button_angry.pack(pady=5)

        self.back_to_main_page()


    def sleep(self):
        self.master.clear_frames()
        self.master.title("Sleep")

        sleep_info = """
        La calidad del sueño es crucial para la salud y el bienestar.
        Asegúrate de tener un ambiente propicio para dormir, con una temperatura
        adecuada y sin distracciones. Intenta mantener un horario regular de sueño
        para mejorar la calidad y la cantidad de descanso.
        """
        label = tk.Label(self.master, text=sleep_info, font=("Helvetica", 12), justify="left", wraplength=400)
        label.pack(pady=10)

        self.back_to_main_page()


if __name__ == "__main__":
    app = App()
    app.mainloop()