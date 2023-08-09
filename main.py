import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

# Generate list of text filepath
filepaths = glob.glob("TextFiles/*.txt")

# Create a pdf file
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    # Extract the filename from filepath
    filename = Path(filepath).stem

    # Generate PDF page
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=0, h=12, txt=filename.capitalize(), ln=1)

pdf.output("output.pdf")

