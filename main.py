import pandas as pd
from fpdf import FPDF
import glob

filepaths = glob.glob("TextFiles/*.txt")

for filepath in filepaths:
    print(filepath)

