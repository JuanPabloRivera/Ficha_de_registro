
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color
from reportlab.lib.units import inch
#from docx import Document

class FileGenerator:
    def createPDF(id, forename, surname, category):
        #Creating file
        canvas = Canvas(f"reconocimiento-{id}.pdf", pagesize=letter)
        width, height = letter

        #Background image and rectangle for information
        im = ImageReader("bg_image.jpg")
        canvas.drawImage(image=im, x=0, y=0, width=width, height=height)
        gray50transparent = Color(160, 160, 160, alpha=0.75)
        canvas.setFillColor(gray50transparent)
        canvas.rect(0.5*inch, 2*inch, width-inch, height-4*inch, fill=True, stroke=False)

        #Text
        canvas.setFont('Helvetica', 20)
        canvas.setFillColor(Color(0,0,0, alpha=1)) #Black

        canvas.drawCentredString(width/2, 8*inch, "Torneo de Programación Competitiva")
        canvas.drawCentredString(width/2, 7.5*inch, "Copa Guadalajara 2021")
        canvas.drawCentredString(width/2, 6*inch, "Se otorga el reconocimiento a:")
        canvas.setFont('Helvetica-Bold', 20)
        canvas.drawCentredString(width/2, 5.5*inch, f'{forename} {surname}')
        canvas.setFont('Helvetica', 20)
        canvas.drawCentredString(width/2, 4*inch, f"Por su participación en la categoría {category}")
        canvas.drawCentredString(width/2, 3.5*inch, ' en la copa de programación competitiva')
        canvas.drawCentredString(width/2, 3*inch, 'Guadalajara 2021.')
        
        #Closing file
        canvas.save()

    def createTXT(id, forename, surname, category):
        pass

    def createDOCX(id, forename, surname, category):
        pass