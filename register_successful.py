import tkinter as tk
from tkinter import ttk
from reportlab.pdfgen.canvas import Canvas

class RegisterSuccessful(tk.Tk):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        label = tk.Label(self, text='Ha sido registrado exitosamente\n¿Desea recibir un reconocimiento de participación?')
        label.grid(row=0, column=0, columnspan=4, padx=15, pady=15, sticky='EW')

        self.rValue = tk.IntVar()
        sRadioButton = ttk.Radiobutton(self, text='Sí', value=0, variable=self.rValue)
        sRadioButton.grid(row=1, column=0, padx=10, pady=10, sticky='EW')
        sRadioButton.bind('<Button-1>', self.adjustFile)
        nRadioButton = ttk.Radiobutton(self, text='No', value=1, variable=self.rValue)
        nRadioButton.grid(row=1, column=1, padx=10, pady=10, sticky='EW')
        nRadioButton.bind('<Button-1>', self.adjustFile)
        self.rValue.set(0)

        formatLabel = tk.Label(self, text='File format: ')
        formatLabel.grid(row=1, column=2, padx=5, pady=10, sticky='EW')
        self.formatCombobox = ttk.Combobox(self, values=['.pdf', '.txt', '.doc'], state='readonly')
        self.formatCombobox.grid(row=1, column=3, padx=10, pady=10, sticky='EW')

        button = ttk.Button(self, text='OK', command=self.finish)
        button.grid(row=2, column=0, columnspan=4, padx=15, pady=15, sticky='EW')
    
    def adjustFile(self, event):
        

    def finish(self):
        self.destroy()
        self.parent.destroy()

#canvas = Canvas("test.pdf")
#canvas.drawString(72, 72, "Hello World")
#canvas.save()