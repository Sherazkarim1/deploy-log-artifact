# PDFlogs.py

import datetime
from fpdf import FPDF  

def generate_pdf_log(log_content, variables):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Deployment Log", ln=True, align="C")
    pdf.set_font("Arial", size=12)
    for key, value in variables.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
    pdf.set_font("Courier", size=10)
    pdf.multi_cell(0, 10, txt=log_content)
    pdf_file = "deployment_log.pdf"
    pdf.output(pdf_file)
    return pdf_file

log_content = """
2024-04-30 11:00: Deployment started
2024-04-30 11:05: Build successful
2024-04-30 11:10: Deployment completed
"""

variables = {
    "Deployment Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "Deployed By": "Your Name",
    "Environment": "Production"
}

pdf_file = generate_pdf_log(log_content, variables)
print(f"PDF log generated: {pdf_file}")
