import pandas as pd
import glob
from fpdf import FPDF
from common import *
from pathlib import Path

filepaths = glob.glob("data/*.xlsx")

for f in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font(family="Arial", size=12)
    pdf.set_text_color(100, 100, 100)
    store = "My Favourite Store.com"
    old_x = pdf.get_x()
    old_y = pdf.get_y()
    pdf.set_x(130)
    pdf.cell(w=0, h=8, txt=f"{store}", ln=True)
    pdf.set_x(old_x)
    pdf.image("data/store.png", w=16, h=16, x=180, y=6)
    pdf.cell(w=0, h=0, ln=True)

    number, date = Path(f).stem.split("-")
    get_header(pdf, f"Invoice {number}")

    pdf.set_font(family="Arial", size=12, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}", border=False, ln=True)

    df = pd.read_excel(f, sheet_name="Sheet 1")
    pdf.set_font(family="Arial", size=8)
    pdf.set_text_color(100, 100, 100)
    for header in [
        "ID",
        "Product name",
        "Amount purchased",
        "Price per unit",
        "Total price",
    ]:
        pdf.cell(
            w=40 if header == "Product name" or header == "Amount purchased" else 20,
            h=5,
            txt=header,
            border=1,
            ln=True if header == "Total price" else False,
        )
    total = 0
    for index, row in df.iterrows():
        pdf.cell(w=20, h=5, txt=str(row["product_id"]), border=1)
        pdf.cell(w=40, h=5, txt=row["product_name"], border=1)
        pdf.cell(w=40, h=5, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=20, h=5, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=20, h=5, txt=str(row["total_price"]), border=1, ln=True)
        total += row["total_price"]
    [
        pdf.cell(
            w=length,
            h=5,
            txt=str(total) if index == 4 else "",
            border=1,
            ln=True if index == 4 else False,
        )
        for index, length in enumerate([20, 40, 40, 20, 20])
    ]
    pdf.cell(w=0, h=10, txt=f"Total price for entire purchase is {total} EUR.", ln=True)

    pdf.output(f"./output/{Path(f).stem}.pdf")
