from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
#from docx import Document

class FileGenerator:
    def createPDF(self):
        canvas = Canvas("reconocimiento.pdf", pagesize=(8.5 * inch, 11 * inch))
        canvas.setFont('Helvetica', 20)
        canvas.drawString(2*inch, 8*inch, "Torneo de Programación Competitiva")
        canvas.drawString(2.7*inch, 7.5*inch, "Copa Guadalajara 2021")
        canvas.drawString(2.4*inch, 6*inch, "Se otorga el reconocimiento a:")
        canvas.setFont('Helvetica-Bold', 20)
        canvas.drawString(2.6*inch, 5.5*inch, f'{self.parent.fornameEntry.get().strip()} {self.parent.surnameEntry.get().strip()}')
        canvas.setFont('Helvetica', 20)
        canvas.drawString(1.5*inch, 4*inch, f"Por su participación en la categoría {self.parent.categoryCombobox.get().lower()}")
        canvas.drawString(0.5*inch, 3.5*inch, ' en la copa de programación competitiva Guadalajara 2021.')
        canvas.save()

    def createTXT(self):
        pass

    def createDOCX(self):
        pass