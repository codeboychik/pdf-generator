def get_header(pdf, text):
    pdf.set_font(family='Arial', style='B', size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=f'{text}', ln=1)


def get_lines(pdf, start, stop, full_page=True):
    for y in range(start, stop, 11):
        pdf.line(10, y, 100 if not full_page else 200, y)


def get_footer(pdf, text):
    pdf.ln(265)
    pdf.set_font(family='Arial', style='', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=f'{text}', ln=1, align='R')


def get_bottom_notes(pdf):
    old_y = pdf.get_y()
    pdf.set_y(220)
    pdf.cell(w=0, h=60, border=1, ln=200)
    pdf.set_y(old_y)
