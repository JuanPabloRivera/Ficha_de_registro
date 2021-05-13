import tkinter as tk
from tkinter import ttk, font
from file_generator import FileGenerator


class ParticipantFound(tk.Tk):
    def __init__(self, parent, idx):
        super().__init__()
        self.idx = idx
        self.dataContainer = parent.dataContainer
        self.winfo_toplevel().title("Participante encontrado")
        self.resizable(0,0)
    
        label = tk.Label(self, text='El participante fue encontrado\nElija el formato en el que desea recibir su reconocimiento')
        label.grid(row=0, column=0, columnspan=2, padx=15, pady=15, sticky='EW')

        formatLabel = tk.Label(self, text='File format: ')
        formatLabel.grid(row=1, column=0, padx=5, pady=10, sticky='EW')
        self.formatCombobox = ttk.Combobox(self, values=['.pdf', '.txt', '.docx'], state='readonly')
        self.formatCombobox.grid(row=1, column=1, padx=10, pady=10, sticky='EW')
        self.formatCombobox.current([0])

        button = ttk.Button(self, text='OK', command=self.finish)
        button.grid(row=2, column=0, columnspan=4, padx=15, pady=15, sticky='EW')

    def finish(self):
        participant = self.dataContainer.participants[self.idx]
        if self.formatCombobox.get() == '.pdf':
            FileGenerator.createPDF(self.idx, participant[0], participant[1], participant[-1].lower())
        elif self.formatCombobox.get() == '.txt':
            FileGenerator.createTXT(self.idx, participant[0], participant[1], participant[-1].lower())
        else:
            FileGenerator.createDOCX(self.idx, participant[0], participant[1], participant[-1].lower())

        self.destroy()
