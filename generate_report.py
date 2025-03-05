import os
import pandas as pd
from fpdf import FPDF

# Load Dataset
df = pd.read_csv(r"C:\Users\madhu\Documents\task 2\data.csv")

# Define PDF Class for Report Formatting
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(200, 10, "Data Analysis Report", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f'Page {self.page_no()}', align="C")

# Initialize PDF Report
pdf = PDF()
pdf.add_page()

# Add Title
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Summary Statistics", ln=True)

# Compute Summary Statistics for Numerical Columns
pdf.set_font("Arial", size=10)
numeric_columns = df.select_dtypes(include=['number']).columns
summary = df[numeric_columns].describe().to_dict()

# Add Summary Statistics to PDF
for col in numeric_columns:
    pdf.cell(200, 10, f"{col}: Mean={summary[col]['mean']:.2f}, Min={summary[col]['min']:.2f}, Max={summary[col]['max']:.2f}", ln=True)

# Add Salary Histogram (if exists)
if os.path.exists("salary_histogram.png"):
    pdf.image("salary_histogram.png", x=50, w=100)
else:
    print("Warning: 'salary_histogram.png' not found!")

# Add a New Page for Department Salary Chart
pdf.add_page()
pdf.cell(200, 10, "Average Salary by Department", ln=True)

# Add Department Salary Bar Chart (if exists)
if os.path.exists("department_salary.png"):
    pdf.image("department_salary.png", x=50, w=100)
else:
    print("Warning: 'department_salary.png' not found!")

# Save the PDF Report
pdf.output("Report.pdf")
print("PDF Report Generated Successfully!")
