import tkinter as tk
from tkinter import ttk, font
from invalid_id import InvalidId
from file_generator import FileGenerator

class AcknowledgeWindow(tk.Tk):
    def __init__(self, dataContainer):
        super().__init__()

        self.dataContainer = dataContainer
        self.winfo_toplevel().title("Premiar partipantes")
        self.resizable(0,0)

        label1 = tk.Label(self, text='Ingrese el ID del participante del 1er lugar')
        label1.grid(row=0, column=0, padx=15, pady=15, sticky='NSEW')

        label2 = tk.Label(self, text='Ingrese el ID del participante del 2do lugar')
        label2.grid(row=1, column=0, padx=15, pady=15, sticky='NSEW')

        label3 = tk.Label(self, text='Ingrese el ID del participante del 3er lugar')
        label3.grid(row=2, column=0, padx=15, pady=15, sticky='NSEW')

        self.idEntry1 = ttk.Entry(self, width=4)
        self.idEntry1.grid(row=0, column=1, padx=15, pady=10, sticky='EW')

        self.idEntry2 = ttk.Entry(self, width=4)
        self.idEntry2.grid(row=1, column=1, padx=15, pady=10, sticky='EW')

        self.idEntry3 = ttk.Entry(self, width=4)
        self.idEntry3.grid(row=2, column=1, padx=15, pady=10, sticky='EW')

        acknowledgeButton = tk.Button(self, text='BUSCAR', command=self.acknowledge)
        acknowledgeButton.grid(row=3, column=0, padx=15, pady=15, sticky='NSEW')

        cancelButton = tk.Button(self, text='CANCELAR', command=self.destroy)
        cancelButton.grid(row=3, column=1, padx=15, pady=15, sticky='NSEW')

    def acknowledge(self):
        id1 = self.idEntry1.get()
        id2 = self.idEntry2.get()
        id3 = self.idEntry3.get()

        if (id1 in self.dataContainer.participants.keys()) and (id2 in self.dataContainer.participants.keys()) and (id3 in self.dataContainer.participants.keys()):
            FileGenerator.createAcknowledge(id1, self.dataContainer.participants[id1], id2, self.dataContainer.participants[id2], id3, self.dataContainer.participants[id3])
            self.destroy()
        else:
            invalid = InvalidId()
            invalid.mainloop()
