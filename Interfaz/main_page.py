import tkinter as tk
from tkinter import PhotoImage
from log_in import LogInWindow
from sign_up import SignInWindow

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Page")
        self.master.geometry("340x667")  # width x height, in pixels

        self.imagen = PhotoImage(file="./Archivos/Background2.png")
        
        self.label_imagen = tk.Label(self.master, image=self.imagen)
        self.label_imagen.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_buttons()

    def create_buttons(self):
        self.button_login = tk.Button(self.master, text="Log In", command=self.open_login_window, fg="black")
        self.button_login.place(x=80, y=340)

        self.button_signup = tk.Button(self.master, text="Sign Up", command=self.open_signup_window, fg="black")
        self.button_signup.place(x=180, y=340)

    def open_login_window(self):
        self.master.destroy()
        login_window = tk.Tk()
        login_window.title("Log In")
        login_app = LogInWindow(login_window)
        login_window.mainloop()

    def open_signup_window(self):
        self.master.destroy()
        signup_window = tk.Tk()
        signup_window.title("Sign Up")
        signup_app = SignInWindow(signup_window)
        signup_window.mainloop()

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
