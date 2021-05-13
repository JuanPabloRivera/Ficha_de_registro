import tkinter as tk
from tkinter import ttk, font
from invalid_id import InvalidId
from participant_found import ParticipantFound

class SearchWindow(tk.Tk):
    def __init__(self, dataContainer):
        super().__init__()

        self.dataContainer = dataContainer

        self.winfo_toplevel().title("Buscar partipante")
        self.resizable(0,0)

        label = tk.Label(self, text='Ingrese el id del participante\nque desea buscar')
        label.grid(row=0, column=0, padx=15, pady=15, sticky='NSEW')

        self.idEntry = ttk.Entry(self, width=4)
        self.idEntry.grid(row=0, column=1, padx=15, pady=10, sticky='EW')

        searchButton = tk.Button(self, text='BUSCAR', command=self.search)
        searchButton.grid(row=1, column=0, padx=15, pady=15, sticky='NSEW')

        cancelButton = tk.Button(self, text='CANCELAR', command=self.destroy)
        cancelButton.grid(row=1, column=1, padx=15, pady=15, sticky='NSEW')

    def search(self):
        idx = self.idEntry.get()

        if idx in self.dataContainer.participants.keys():
            info = ParticipantInfo(idx, self.dataContainer)
            while info.running:
                info.update()
            info.destroy()
            found = ParticipantFound(self, idx)
            while found.running:
                found.update()
            found.destroy()
            self.destroy()
        else:
            invalid = InvalidId()
            invalid.mainloop()

class ParticipantInfo(tk.Tk):
    def __init__(self, idx, dataContainer):
        super().__init__()

        self.running = True

        labelName = ['Nombre', 'Apellido', 'CURP', 'SEXO', 'ESTADO', 'CIUDAD', 'COLONIA', 'CALLE', 'NÚMERO', 'C.P.','ESTUDIANTE', 'ESCUELA', 'CATEGORÍA']

        for i, name in enumerate(labelName):
            label = tk.Label(self, text=f'{name}: ')
            label.grid(row=i, column=0, padx=25, pady=10, sticky='NSEW')

            label = tk.Label(self, text=f'{dataContainer.participants[idx][i]}')
            label.grid(row=i, column=1, padx=25, pady=10, sticky='NSEW')

        button = tk.Button(self, text='OK', command=self.exit)
        button.grid(row=13, column=0, columnspan=2, padx=25, pady=10, sticky='NSEW')

    def exit(self):
        self.running = False