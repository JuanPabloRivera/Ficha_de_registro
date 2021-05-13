import tkinter as tk
from tkinter import ttk, font

class DataContainer(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, labelanchor='n', text='Registro de participantes', font=font.Font(family='Helvetica', size='12', weight='bold'))

        self.participantNumber = 0
        self.participants = dict()
        self.entries = []

        entryWidth = [4,12,12,12,3,12,12,12,12,7,7,3,12,12]
        entryName = ['#', 'Nombre', 'Apellido', 'CURP', 'SEXO', 'ESTADO', 'CIUDAD', 'COLONIA', 'CALLE', 'NÚMERO', 'C.P.','ESTUDIANTE', 'ESCUELA', 'CATEGORÍA']

        # Column headers
        for k in range(14):
            e = tk.Entry(self, width=entryWidth[k])
            e.grid(row=0, column=k, sticky='NSEW')
            e.insert(0, entryName[k])
            e.config(state=tk.DISABLED)

        # Spaces for 24 participants
        for i in range(1,24):
            participant = []
            for j in range(14):
                e = tk.Entry(self, width=entryWidth[j], state=tk.DISABLED)
                e.grid(row=i, column=j, sticky='NSEW')
                participant.append(e)
            self.entries.append(participant)

    def addParticipant(self, data):
        self.participantNumber += 1
        self.participants[self.participantNumber] = data
        self.updateContainer()

    def removeParticipant(self, id):
        self.participants.pop(id)
        self.updateContainer()

    def updateContainer(self):
        # Clearing the entries 
        for entry in self.entries:
            for field in entry:
                field.config(state=tk.NORMAL)
                field.delete(0, tk.END)

        for idx, (key, data) in enumerate(self.participants.items()):
            entry = self.entries[idx]
            
            # Writing the new information
            entry[0].insert(0, str(key))
            entry[1].insert(0, data[0])
            entry[2].insert(0, data[1])
            entry[3].insert(0, data[2])
            entry[4].insert(0, data[3])
            entry[5].insert(0, data[4])
            entry[6].insert(0, data[5])
            entry[7].insert(0, data[6])
            entry[8].insert(0, data[7])
            entry[9].insert(0, data[8])
            entry[10].insert(0, data[9])
            entry[11].insert(0, data[10])
            entry[12].insert(0, data[11])
            entry[13].insert(0, data[12])

        for entry in self.entries:
            for field in entry: field.config(state=tk.DISABLED)