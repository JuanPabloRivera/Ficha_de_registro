import tkinter as tk
from tkinter import ttk
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch

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
        self.formatCombobox = ttk.Combobox(self, values=['.pdf', '.txt', '.doc'], state='readonly')
        self.formatCombobox.grid(row=1, column=3, padx=10, pady=10, sticky='EW')
        self.formatCombobox.current([0])

        button = ttk.Button(self, text='OK', command=self.finish)
        button.grid(row=2, column=0, columnspan=4, padx=15, pady=15, sticky='EW')

    def finish(self):
        if self.fileValue.get():
            if self.formatCombobox.get() == '.pdf':
                self.createPDF()
            elif self.formatCombobox.get() == '.txt':
                pass
            else:
                pass

        self.destroy()
        self.parent.destroy()

    def createPDF(self):
        canvas = Canvas("reconocimiento.pdf", pagesize=(8.5 * inch, 11 * inch))
        canvas.setFont('Helvetica', 20)
        canvas.drawString(2*inch, 8*inch, "Torneo de Programación Competitiva")
        canvas.drawString(2.7*inch, 7.5*inch, "Copa Guadalajara 2021")
        canvas.drawString(2.4*inch, 6*inch, f"Se otorga el reconocimiento a:")
        canvas.setFont('Helvetica-Bold', 20)
        canvas.drawString(2.6*inch, 5.5*inch, f'{self.parent.mainFrame.fornameEntry.get().strip()} {self.parent.mainFrame.surnameEntry.get().strip()}')
        canvas.setFont('Helvetica', 20)
        canvas.drawString(1.5*inch, 4*inch, f"Por su participación en la categoría {self.parent.mainFrame.categoryCombobox.get().lower()}")
        canvas.drawString(0.5*inch, 3.5*inch, ' en la copa de programación competitiva Guadalajara 2021.')
        canvas.save()