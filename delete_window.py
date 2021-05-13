import tkinter as tk
from tkinter import ttk, font
from invalid_id import InvalidId

class DeleteWindow(tk.Tk):
    def __init__(self, dataContainer):
        super().__init__()
        self.dataContainer = dataContainer

        self.winfo_toplevel().title("Eliminar partipante")
        self.resizable(0,0)

        label = tk.Label(self, text='Ingrese el id del participante\nque desea eliminar')
        label.grid(row=0, column=0, padx=15, pady=15, sticky='NSEW')

        self.idEntry = ttk.Entry(self, width=4)
        self.idEntry.grid(row=0, column=1, padx=15, pady=10, sticky='EW')

        deleteButton = tk.Button(self, text='ELIMINAR', command=self.delete)
        deleteButton.grid(row=1, column=0, padx=15, pady=15, sticky='NSEW')

        cancelButton = tk.Button(self, text='CANCELAR', command=self.destroy)
        cancelButton.grid(row=1, column=1, padx=15, pady=15, sticky='NSEW')

    def delete(self):
        idx = self.idEntry.get()

        if idx in self.dataContainer.participants.keys():
            self.dataContainer.removeParticipant(idx)
            self.destroy()
        else:
            invalid = InvalidId()
            invalid.mainloop()