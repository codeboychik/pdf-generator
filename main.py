from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(False)
data = pd.read_csv('topics.csv')


def get_lines(start, stop, full_page=True):
    for y in range(start, stop, 11):
        pdf.line(10, y, 100 if not full_page else 200, y)


def get_footer(text):
    pdf.ln(265)
    pdf.set_font(family='Arial', style='', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=f'{text}', ln=1, align='R')


def get_bottom_notes():
    old_y = pdf.get_y()
    pdf.set_y(220)
    pdf.cell(w=0, h=60, border=1, ln=200)
    pdf.set_y(old_y)


for index, row in data.iterrows():
    pdf.add_page()

    # header
    pdf.set_font(family='Arial', style='', size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=f'{row["Order"]}.{row["Topic"]}', ln=1)
    pdf.line(10, 22, 200, 22)

    # half-page lines
    get_lines(start=22, stop=110, full_page=False)

    # full-page lines
    get_lines(start=110, stop=220, full_page=True)

    # bottom notes
    get_bottom_notes()

    # footer
    get_footer(row["Topic"])

    for i in range(row['Pages'] - 1):
        pdf.add_page()

        # half-page lines
        get_lines(start=22, stop=110, full_page=False)

        # full-page lines
        get_lines(start=110, stop=220, full_page=True)

        # bottom notes
        get_bottom_notes()

        get_footer(text=row['Topic'])

pdf.output('o.pdf')
