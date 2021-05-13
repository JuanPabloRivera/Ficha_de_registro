import tkinter as tk
from tkinter import ttk, font
from data_container import DataContainer
from search_window import SearchWindow
from delete_window import DeleteWindow
from acknowledge_window import AcknowledgeWindow

class DataFrame(tk.LabelFrame):
    def __init__(self, parent, showRegister):
        super().__init__()

        self.dataContainer = DataContainer(self)
        self.dataContainer.grid(row=0, column=0, columnspan=4, padx=25, pady=(25,0), sticky='NSEW')

        registerButton = tk.Button(self, text='REGISTRO', bg='#ffbf45', font=font.Font(family='Helvetica', size='12', weight='bold'), command=showRegister)
        registerButton.grid(row=1, column=0, padx=25, pady=10, sticky='NSEW')

        searchButton = tk.Button(self, text="BUSCAR", bg='#4a5fff', font=font.Font(family='Helvetica', size='12', weight='bold'), command=self.search)
        searchButton.grid(row=1, column=1, padx=25, pady=10, sticky='NSEW')

        deleteButton = tk.Button(self, text='ELIMINAR', bg='#ed3833', font=font.Font(family='Helvetica', size='12', weight='bold'), command=self.delete)
        deleteButton.grid(row=1, column=2, padx=25, pady=10, sticky='NSEW')

        acknowledgmentButton = tk.Button(self, text='PREMIAR', bg='#4ca0ff', font=font.Font(family='Helvetica', size='12', weight='bold'), command=self.acknowledge)
        acknowledgmentButton.grid(row=1, column=3, padx=25, pady=10, sticky='NSEW')

    def search(self):
        search = SearchWindow(self.dataContainer)
        search.mainloop()

    def delete(self):
        delete = DeleteWindow(self.dataContainer)
        delete.mainloop()

    def acknowledge(self):
        acknowledge = AcknowledgeWindow(self.dataContainer)
        acknowledge.mainloop()