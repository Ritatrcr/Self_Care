#Object client with atributes: name, username, email, password 
# setters, getters y toString

class Client:
    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def set_name(self, name):
        self.name = name

    def set_username(self, username):
        self.username = username

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def __str__(self):
        return f"Name: {self.name}, Username: {self.username}, Email: {self.email}, Password: {self.password}"