import tkinter as tk
from tkinter import ttk
from file_generator import FileGenerator

class RegisterSuccessful(tk.Tk):
    def __init__(self, parent):
        super().__init__()

        self.winfo_toplevel().title("Registro exitoso")
        self.resizable(0,0)
        self.dataContainer = parent.dataContainer
    
        label = tk.Label(self, text='Ha sido registrado exitosamente\nElija el formato en el que desea recibir su reconocimiento')
        label.grid(row=0, column=0, columnspan=2, padx=15, pady=15, sticky='EW')

        formatLabel = tk.Label(self, text='File format: ')
        formatLabel.grid(row=1, column=0, padx=5, pady=10, sticky='EW')
        self.formatCombobox = ttk.Combobox(self, values=['.pdf', '.txt', '.docx'], state='readonly')
        self.formatCombobox.grid(row=1, column=1, padx=10, pady=10, sticky='EW')
        self.formatCombobox.current([0])

        button = ttk.Button(self, text='OK', command=self.finish)
        button.grid(row=2, column=0, columnspan=4, padx=15, pady=15, sticky='EW')

    def finish(self):
        idx = str(self.dataContainer.participantNumber)
        participant = self.dataContainer.participants[idx]
        if self.formatCombobox.get() == '.pdf':
            FileGenerator.createPDF(idx, participant[0], participant[1], participant[-1].lower())
        elif self.formatCombobox.get() == '.txt':
            FileGenerator.createTXT(idx, participant[0], participant[1], participant[-1].lower())
        else:
            FileGenerator.createDOCX(idx, participant[0], participant[1], participant[-1].lower())

        self.destroy()