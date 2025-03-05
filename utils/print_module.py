from reportlab.lib.pagesizes import A5
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.graphics.barcode import code128  # For barcode generation
from win32 import win32api, win32print
import os
from utils import settings
import datetime
from time import sleep

def create_production_label(datetime: datetime.datetime, lot: int, article_description: str,
                            poids: int, numero_pesee: int):

    item_style = ParagraphStyle(
        name="ItemStyle",
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=10,
        wordWrap='LTR',
        alignment=0
    )

    # Define custom margins (e.g., 10 mm on all sides)
    left_margin = 20 * mm
    right_margin = 20 * mm
    top_margin = 0 * mm
    bottom_margin = 10 * mm

    # Path to the image
    image_path = os.path.abspath(os.path.join(settings.path_name,"static\\logo_ReMatch.jpg"))

    # Create a PDF file
    pdf_filename = os.path.abspath(os.path.join(settings.path_name,"static\\etiquette_production.pdf"))
    doc = SimpleDocTemplate(pdf_filename,
                            pagesize=A5,
                            leftMargin=left_margin,
                            rightMargin=right_margin,
                            topMargin=top_margin,
                            bottomMargin=bottom_margin)

    # Create a list to hold the content of the PDF
    content = []

    # Define styles
    styles = getSampleStyleSheet()

    # Create a table to align the header text and image at the same height
    header_table_data = [
        [Paragraph("Re Match France SAS<br/>15 rue de Johannesbourg<br/>FR-67150 Erstein<br/>France", 
                styles["Normal"]), Image(image_path, width=100, height=50)], 
                ["",f"""Date/Time: \n {datetime}"""]
    ]

    # Define the table style for the header
    header_table_style = TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),  # Align content to the top
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),    # Align text to the left
        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),   # Align image to the right
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),  # Add padding below the header
    ])

    # Create the header table
    header_table = Table(header_table_data, colWidths=[doc.width * 0.7, doc.width * 0.3])  # Adjust column widths as needed
    header_table.setStyle(header_table_style)
    content.append(header_table)

    content.append(Spacer(3, 30))  # Add some space after the Date/Time

    # Create a table for the remaining data
    table_data = [
        ["Batch", lot],
        ["Item", Paragraph(article_description, item_style)],
        ["Kg", poids],
        ["", ""],
        ["", numero_pesee]
    ]

    #Generate the barcode
    barcode = code128.Code128(numero_pesee, barHeight=40, barWidth=2) 
    # Replace the "Barcode" row with the actual barcode
    table_data[3][1] = barcode

    # Define the table width (120% of the page width)
    table_width = doc.width * 1.2

    # Define the table style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.transparent),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('VALIGN', (1, 4), (1, 4), 'TOP'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -2), 25), #Right Column
        ('FONTSIZE', (0, 0), (0, -1), 12), #Left column
        ('GRID', (0, 0), (3, 3), 1, colors.black),
    ])

    # Create the table
    table = Table(table_data, colWidths=[table_width * 0.2, table_width * 0.8], rowHeights=60)  # Adjust column widths as needed
    table.setStyle(table_style)
    content.append(table)

    # Build the PDF
    doc.build(content)
    print_label(filename=pdf_filename)

def print_label(filename):
    #TODO: be sure to select the default printer
    win32print.SetDefaultPrinter("Brother HL-L2445DW")
    win32api.ShellExecute(0, "print", filename, None, ".", False) #Print based on the default printer 

if __name__ =="__main__":
    pass
    #printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
    #for itrems in printers:
    #    print(itrems)
    #print(win32print.GetDefaultPrinter())
    #print(win32print.GetDefaultPrinterW())
    #win32api.ShellExecute(0, "print", ".\\static\\etiquette_production.pdf", None, ".", False)
    #settings.global_init("C:\\Users\\MarcelBeyer\\Marcel\\Programmes\\RematchInternal\\")
    #list_items = [
    #    [330110276,3301116431,1020,"RUBBER MIX 0.8 - 2.5 MM"],
    #    [990110478,3301121317,1009,"RUBBER MIX 0.8 - 2.0 MM"]
    #]

    #for items in list_items:
    #    create_production_label(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
    #                            items[0], items[3], items[2], items[1])
    #    sleep(15)   
