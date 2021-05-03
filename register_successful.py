import tkinter as tk
from tkinter import ttk

class RegisterSuccessful(tk.Tk):
    def __init__(self, parent):
        super().__init__()

        self.resizable(0,0)
        self.parent = parent
    
        label = tk.Label(self, text='Ha sido registrado exitosamente\n¿Desea recibir un reconocimiento de participación?')
        label.grid(row=0, column=0, columnspan=4, padx=15, pady=15, sticky='EW')

        self.fileValue = tk.IntVar(self)
        yesRadio = ttk.Radiobutton(self, text='Sí', value=1, variable=self.fileValue)
        yesRadio.grid(row=1, column=0, padx=10, pady=10, sticky='EW')
        noRadio = ttk.Radiobutton(self, text='No', value=0, variable=self.fileValue)
        noRadio.grid(row=1, column=1, padx=10, pady=10, sticky='EW')

        formatLabel = tk.Label(self, text='File format: ')
        formatLabel.grid(row=1, column=2, padx=5, pady=10, sticky='EW')
        self.formatCombobox = ttk.Combobox(self, values=['.pdf', '.txt', '.docs'], state='readonly')
        self.formatCombobox.grid(row=1, column=3, padx=10, pady=10, sticky='EW')
        self.formatCombobox.current([0])

        button = ttk.Button(self, text='OK', command=self.finish)
        button.grid(row=2, column=0, columnspan=4, padx=15, pady=15, sticky='EW')

    def finish(self):
        if self.fileValue.get():
            if self.formatCombobox.get() == '.pdf':
                pass
            elif self.formatCombobox.get() == '.txt':
                pass
            else:
                pass

        self.destroy()