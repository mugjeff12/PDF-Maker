from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")
#p=portrait or L= landscape
for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row["Topic"],align="L",ln=1,border=0)
    pdf.line(10,22,200,22)
pdf.output("output.pdf")

#w=0 makes sure that the maximum width is achieved
#border = 1 , makes sure the borders are visible
#ln=1 makes sure the next cell moves to the next linr