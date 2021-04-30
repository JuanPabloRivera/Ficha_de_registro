import tkinter as tk
from main_frame import MainFrame
from reportlab.pdfgen.canvas import Canvas

class Registro(tk.Tk):
    def __init__(self):
        super().__init__()

        self.winfo_toplevel().title("Registro")
        #self.geometry('500x500')
        self.resizable(0,0)
        mainFrame = MainFrame(self)
        mainFrame.grid(row=0, column=0, padx=25, pady=25, sticky='NSEW')

        

app = Registro()
app.mainloop()

#canvas = Canvas("test.pdf")
#canvas.drawString(72, 72, "Hello World")
#canvas.save()
