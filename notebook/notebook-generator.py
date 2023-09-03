from fpdf import FPDF
import pandas as pd
from common import *

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(False)
data = pd.read_csv('data/topics.csv')

for index, row in data.iterrows():
    pdf.add_page()

    # header
    get_header(pdf, f"{row['Order']}.{row['Topic']}")

    pdf.line(10, 22, 200, 22)

    # half-page lines
    get_lines(pdf, start=22, stop=110, full_page=False)

    # full-page lines
    get_lines(pdf, start=110, stop=220, full_page=True)

    # bottom notes
    get_bottom_notes(pdf)

    # footer
    get_footer(pdf, row["Topic"])

    for i in range(row['Pages'] - 1):
        pdf.add_page()

        # half-page lines
        get_lines(pdf, start=22, stop=110, full_page=False)

        # full-page lines
        get_lines(pdf, start=110, stop=220, full_page=True)

        # bottom notes
        get_bottom_notes(pdf)

        get_footer(pdf, text=row['Topic'])

pdf.output('o.pdf')
