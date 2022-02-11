# Program 9: PDF Resume Creator

from fpdf import FPDF

import json


class PDF(FPDF):
    def header(self):
        self.image("picture.png", 150, 15, 50)
        self.set_font("Times", "B", 26)
        self.ln()

pdf = PDF('P', 'mm', 'Letter')
pdf.add_page()

with open("resume.json") as f:
    data = json.load(f)
    
for info in data:
    pdf.ln(30)
    pdf.set_font("Times", 'B', 24)
    pdf.cell(100, 5, info["name"], ln=True)
    pdf.set_font("Times", 'B', 14)
    pdf.cell(60, 5, info["address"], ln=True)
    pdf.cell(50, 5, info["phone_number"], ln=True)
    pdf.cell(40, 5, info["email"], ln=True)
    
    pdf.ln(13)
    pdf.set_font("Times", 'B', 12)
    pdf.cell(100, 10, "Objectives: ", 0, 0)
    
    pdf.ln(8)
    pdf.set_font("Times", "", 12)
    pdf.cell(100, 5, info["objective"],ln=True)
    pdf.cell(100, 5, info["obj2"],ln=True)

    pdf.ln(12)
    pdf.set_font("Times", "B", 14)
    pdf.cell(150, 10, "Personal Data", 0, 0, "L")
    
    pdf.ln(8)
    pdf.set_font("Times", "", 12)
    pdf.cell(60, 8, "Citizenship: ", 0, 0, "L")
    pdf.cell(60, 8, info["citizenship"], ln=True)
    pdf.cell(60, 8, "Age: ", 0, 0, "L")
    pdf.cell(60, 8, info["age"], ln=True)
    pdf.cell(60, 8, "Civil Status: ", 0, 0, "L")
    pdf.cell(60, 8, info["civil_status"], ln=True)
    pdf.cell(60, 8, "Religion: ", 0, 0, "L")
    pdf.cell(60, 8, info["religion"], ln=True)
    pdf.cell(60, 8, "Language Written and Spoken: ", 0, 0, "L")
    pdf.cell(60, 8, info["language"], ln=True)

    pdf.ln(12)
    pdf.set_font("Times", "B", 14)
    pdf.cell(150, 10, "Special Skills", 0, 0, "L")
    
    pdf.ln(8)
    pdf.set_font("Times", "", 12)
    for skill in info["skills"]:
        pdf.cell(60, 8, f"> {skill}", ln=True)
    
    pdf.ln(12)
    pdf.set_font("Times", "B", 14)
    pdf.cell(150, 10, "Educational Attainment", 0, 0, "L")
    pdf.set_font("Times", "", 12)
    
    pdf.ln(8)
    pdf.set_font("Times","", 12)
    for educ in info["education"]:
        pdf.set_font("Times","B", 12)
        pdf.cell(60, 8, f"- {educ['school']}", ln=True)
        pdf.set_font("Times","", 12)
        pdf.cell(60, 8, f"- {educ['year']}", ln=True)
        
pdf.output("CARANDANG_KYLEKRYZEL.pdf")
# You can replace the pdf name with a file name you'd like