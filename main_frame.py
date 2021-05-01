import tkinter as tk
from tkinter import ttk, font


class MainFrame(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, labelanchor='n', text='Ficha de registro para participantes', font=font.Font(family='Helvetica', size='12', weight='bold'))

        fontStyle = font.Font(family='Helvetica', size='10', weight='bold')
        fontStyle2 = font.Font(family='Helvetica', size='10')


        fornameLabel = tk.Label(self, text="Nombre: ", font=fontStyle)
        fornameLabel.grid(row=0, column=0, padx=10, pady=10, sticky='EW')
        self.fornameEntry = ttk.Entry(self, font=fontStyle2)
        self.fornameEntry.grid(row=0, column=1, columnspan=3, padx=10, pady=10, sticky='EW')

        surnameLabel = tk.Label(self, text="Apellido: ", font=fontStyle)
        surnameLabel.grid(row=1, column=0, padx=10, pady=10, sticky='EW')
        self.surnameEntry = ttk.Entry(self, font=fontStyle2)
        self.surnameEntry.grid(row=1, column=1, columnspan=3, padx=10, pady=10, sticky='EW')
        
        curpLabel = tk.Label(self, text='CURP: ', font=fontStyle)
        curpLabel.grid(row=2, column=0, padx=10, pady=10, sticky='EW')
        self.curpEntry = ttk.Entry(self, font=fontStyle2)
        self.curpEntry.grid(row=2, column=1, columnspan=3, padx=10, pady=10, sticky='EW')

        sexLabel = tk.Label(self, text='Sexo: ', font=fontStyle)
        sexLabel.grid(row=3, column=0, padx=10, pady=10, sticky='EW')
        self.sexValue = tk.IntVar(self)
        self.sexValue.set(1)
        mRadiobutton = ttk.Radiobutton(self, text='Masculino', value=1, variable=self.sexValue)
        mRadiobutton.grid(row=3, column=1, padx=10, pady=10, sticky='EW')
        fRadiobutton = ttk.Radiobutton(self, text='Femenino', value=0, variable=self.sexValue)
        fRadiobutton.grid(row=3, column=3, padx=(10,50), pady=10, sticky='EW')

        stateLabel = tk.Label(self, text='Estado: ', font=fontStyle)
        stateLabel.grid(row=4, column=0, padx=10, pady=10, sticky='EW')
        self.stateEntry = ttk.Entry(self, font=fontStyle2)
        self.stateEntry.grid(row=4, column=1, padx=10, pady=10, sticky='EW')

        cityLabel = tk.Label(self, text='Ciudad: ', font=fontStyle)
        cityLabel.grid(row=4, column=2, padx=10, pady=10, sticky='EW')
        self.cityEntry = ttk.Entry(self, font=fontStyle2)
        self.cityEntry.grid(row=4, column=3, padx=10, pady=10, sticky='EW')

        blockLabel = tk.Label(self, text='Colonia: ', font=fontStyle)
        blockLabel.grid(row=6, column=0, padx=10, pady=10, sticky='EW')
        self.blockEntry = ttk.Entry(self, font=fontStyle2)
        self.blockEntry.grid(row=6, column=1, columnspan=3, padx=10, pady=10, sticky='EW')

        streetLabel = tk.Label(self, text='Calle: ', font=fontStyle)
        streetLabel.grid(row=7, column=0, padx=10, pady=10, sticky='EW')
        self.streetEntry = ttk.Entry(self, font=fontStyle2)
        self.streetEntry.grid(row=7, column=1, columnspan=3, padx=10, pady=10, sticky='EW')

        numberLabel = tk.Label(self, text='Número: ', font=fontStyle)
        numberLabel.grid(row=8, column=0, padx=10, pady=10, sticky='EW')
        self.numberEntry = ttk.Entry(self, font=fontStyle2)
        self.numberEntry.grid(row=8, column=1, padx=10, pady=10, sticky='EW')

        zipLabel = tk.Label(self, text='C.P: ', font=fontStyle)
        zipLabel.grid(row=8, column=2, padx=10, pady=10, sticky='EW')
        self.zipEntry = ttk.Entry(self, font=fontStyle2)
        self.zipEntry.grid(row=8, column=3, padx=10, pady=10, sticky='EW')

        studentLabel = tk.Label(self, text='Estudiante: ', font=fontStyle)
        studentLabel.grid(row=9, column=0, padx=10, pady=10, sticky='EW')
        self.studentValue = tk.IntVar()
        self.studentValue.set(0)
        sRadioButton = ttk.Radiobutton(self, text='Sí', value=0, variable=self.studentValue)
        sRadioButton.grid(row=9, column=1, padx=10, pady=10, sticky='EW')
        sRadioButton.bind('<Button-1>', self.adjustSchool)
        nRadioButton = ttk.Radiobutton(self, text='No', value=1, variable=self.studentValue)
        nRadioButton.grid(row=9, column=3, padx=10, pady=10, sticky='EW')
        nRadioButton.bind('<Button-1>', self.adjustSchool)

        schoolLabel = tk.Label(self, text='Escuela: ', font=fontStyle)
        schoolLabel.grid(row=10, column=0, padx=10, pady=10, sticky='EW')
        self.schoolEntry = ttk.Entry(self, font=fontStyle2)
        self.schoolEntry.grid(row=10, column=1, padx=10, pady=10, sticky='EW')

        categoryLabel = tk.Label(self, text='Categoría: ', font=fontStyle)
        categoryLabel.grid(row=10, column=2, padx=10, pady=10, sticky='EW')
        self.categoryCombobox = ttk.Combobox(self, values=['Infantil', 'Aficionados', 'Avanzado', 'Libre'], state='readonly')
        self.categoryCombobox.grid(row=10, column=3, padx=10, pady=10, sticky='EW')
        self.categoryCombobox.bind('<<ComboboxSelected>>', self.adjustCost)

        self.costLabel = tk.Label(self, text='Costo de inscripción: $0.00', font=fontStyle)
        self.costLabel.grid(row=11, column=0, columnspan=5, padx=10, pady=10, sticky='EW')

    def data(self):
        data = [self.fornameEntry.get(), self.surnameEntry.get(), self.curpEntry.get(), self.stateEntry.get(), self.cityEntry.get(),
                self.blockEntry.get(), self.streetEntry.get(), self.numberEntry.get(), self.zipEntry.get(), self.categoryCombobox.get()]
        if not self.studentValue.get():
            data.append(self.schoolEntry.get())
        return data

    def adjustSchool(self, event):
        if self.studentValue.get():
            self.schoolEntry.config(state=tk.ACTIVE)
        else: 
            self.schoolEntry.config(state=tk.DISABLED)

    def adjustCost(self, event):
        if self.categoryCombobox.get() == 'Infantil':
            cost = 'Costo de inscripción: $29.95'
        elif self.categoryCombobox.get() == 'Aficionados':
            cost = 'Costo de inscripción: $58.99'
        elif self.categoryCombobox.get() == 'Avanzado':
            cost = 'Costo de inscripción: $89.85'
        else:
            cost = 'Costo de inscripción: $49.95'
        self.costLabel.config(text=cost)