from reportlab.lib.pagesizes import A5
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.graphics.barcode import code128  # For barcode generation
from win32 import win32api, win32print
from model.model_pesee import Pesee
import os


def create_production_label():
    # TODO: change this to be dynamic with the pesee model
    data = {
        "date_time": "06/02/2025 09:22",
        "batch": "330110089",
        "item": "RM Quartz Sand",
        "weight": "750",
        "code": "3301122740"
    }

    # Define custom margins (e.g., 10 mm on all sides)
    left_margin = 20 * mm
    right_margin = 20 * mm
    top_margin = 0 * mm
    bottom_margin = 10 * mm

    # Path to the image
    image_path = "static/logo_ReMatch.jpg"

    # Create a PDF file
    pdf_filename = "static\\etiquette_production.pdf"
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
                ["",f"""Date/Time: \n {data['date_time']}"""]
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
        ["Batch", data["batch"]],
        ["Item", data["item"]],
        ["Kg", data["weight"]],
        ["", ""],
        ["", data["code"]]
    ]

    #Generate the barcode
    barcode = code128.Code128(data["code"], barHeight=40, barWidth=2) 
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

def print_label(filename):
    #TODO: be sure to select the default printer
    #win32print.SetDefaultPrinter(default_printer)
    win32api.ShellExecute(0, "print", filename, None, ".", False) #Print based on the default printer 

if __name__ =="__main__":
    create_production_label()
    print_label(f"{os.path.abspath(os.curdir)}/static/etiquette_production.pdf")
