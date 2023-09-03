import pandas as pd
import glob
from fpdf import FPDF
from common import *
from pathlib import Path

filepaths = glob.glob("data/*.xlsx")

for f in filepaths:
    df = pd.read_excel(f, sheet_name='Sheet 1')

    pdf = FPDF(orientation='P', unit='mm', format='A4')

    pdf.add_page()
    filename = Path(f).stem
    get_header(pdf, f'Invoice {filename.split("-")[0]}')
    pdf.set_font(family='Arial', size=12, style='B')
    pdf.cell(w=50, h=8, txt=f'{filename.split("-")[-1]}', border=False)
    pdf.output(f'./pdfs/{filename}.pdf')




