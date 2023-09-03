from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='P', unit='mm', format='A4')

data = pd.read_csv('topics.csv')

for index, row in data.iterrows():
    pdf.add_page()

    pdf.set_font(family='Arial', style='', size=12)
    pdf.cell(w=0, h=10, txt=f'{row["Order"]}.{row["Topic"]}', ln=1)
    pdf.line(10, 22, 200, 22)
pdf.output('o.pdf')
