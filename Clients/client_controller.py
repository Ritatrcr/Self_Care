
from Clients.client import Cliente

#add client to the list
def add_client(self):
        name = self.entry_name.get()
        username = self.entry_username.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        new_client = Cliente(name, username, email, password)
        self.client_list.append(new_client)

        print("New client added:")
        print(new_client)

        self.clear_entries()
