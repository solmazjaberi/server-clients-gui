import customtkinter as tk
from client import Client

tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")

class LoginSystem:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client = Client(self.server_ip, self.server_port)

        root=tk.CTk()
        root.geometry("900x700")

        frame=tk.CTkFrame(master=root)
        frame.pack(pady=20,padx=60,fill="both",expand=True)

        label = tk.CTkLabel(master=frame, text="Login System")
        label.pack(pady=12,padx=10)

        self.entry1=tk.CTkEntry(master=frame,placeholder_text="Username")
        self.entry1.pack(pady=12,padx=10)

        self.entry2=tk.CTkEntry(master=frame,placeholder_text="Password",show="*")
        self.entry2.pack(pady=12,padx=10)

        button=tk.CTkButton(master=frame,text="Login",command=self.on_login)
        button.pack(pady=12,padx=10)

        checkbox=tk.CTkCheckBox(master=frame,text="Stay Signed-in")
        checkbox.pack(pady=12, padx=10)

        root.mainloop()

    def on_login(self):
        username = self.entry1.get()
        password = self.entry2.get()

        response = self.client.login(username, password)

        if response == "Login Processed":
            print("Login Successful")
        else:
            print("Login Failed")

if __name__ == '__main__':
    login_system = LoginSystem("", "")#you can put your host ip and port number here




