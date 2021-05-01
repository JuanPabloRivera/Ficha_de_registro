import tkinter as tk
from tkinter import font, ttk
from main_frame import MainFrame
from register_failed import RegisterFailed
from register_successful import RegisterSuccessful


class Registro(tk.Tk):
    def __init__(self):
        super().__init__()

        self.winfo_toplevel().title("Registro")
        self.resizable(0,0)
        self.mainFrame = MainFrame(self)
        self.mainFrame.grid(row=0, column=0, padx=25, pady=(25,0), sticky='NSEW')

        self.registerButton = tk.Button(self, text='REGISTRARSE', bg='#4a5fff', font=font.Font(family='Helvetica', size='12', weight='bold'), command=self.validateInfo)
        self.registerButton.grid(row=1, column=0, padx=25, pady=10, sticky='NSEW')

    def validateInfo(self):
        if all(self.mainFrame.data()):
            success = RegisterSuccessful(self)
            success.mainloop()
        else:
            failed = RegisterFailed()
            failed.mainloop()

        

app = Registro()
app.mainloop()