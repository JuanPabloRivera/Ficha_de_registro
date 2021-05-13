import tkinter as tk

class InvalidId(tk.Tk):
    def __init__(self):
        super().__init__()

        self.winfo_toplevel().title("Eliminar partipante")
        self.resizable(0,0)

        label = tk.Label(self, text='ID de participante invalido, por favor ingrese \nel ID de un participante existente.')
        label.grid(row=0, column=0, padx=15, pady=15, sticky='NSEW')

        okButton = tk.Button(self, text='OK', command=self.destroy)
        okButton.grid(row=1, column=0, padx=15, pady=15, sticky='NSEW')