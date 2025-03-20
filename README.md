# Task2_AUTOMATED-REPORT-GENERATION
AUTOMATED REPORT GENERATION

COMPANY:CODTECH IT SOLUTION

NAME:V.MADHUMITHA

INTERN ID:CT04WQE

DOMAIN:PYTHON

DURATION:4 WEEKS

MENTOR:NEELA SANTOSH

DESCRIPTION:

This project consists of two Python scripts:  
1. pd.py – Generates visualizations (Salary Histogram).  
2. generate_report.py– Creates a PDF report with summary statistics and images.  

1. data.csv - The Dataset  
This file contains employee details such as Name, Age, Salary, and Department.  

2. pd.py - Visualization Script
This script reads the dataset and generates a Salary Distribution Histogram using Matplotlib and Seaborn.  

Steps in pd.py:  
  1. Loads the CSV file into a Pandas DataFrame.  
  2. Displays the first few rows (print(df.head())).  
  3. Uses seaborn.histplot() to create a histogram of the **Salary** column.  
  4. Saves the generated histogram as salary_histogram.png.  
  5. Displays the plot using plt.show().  

3. generate_report.py - PDF Report Generation
This script reads the dataset, calculates summary statistics, and generates a PDF report using FPDF.  

- Steps in generate_report.py:  
  1. Reads data.csv into a Pandas DataFrame.  
  2. Defines a PDF class with a header and footer.  
  3. Adds a Summary Statistics section (Mean, Min, Max for numeric columns).  
  4. Inserts images (salary_histogram.png and department_salary.png) into the report.  
  5. Saves the final PDF as Report.pdf.  

Overall Workflow 
1️ Run pd.py → Generates salary_histogram.png.  
2️ Run generate_report.py → Creates Report.pdf with summary & images.  




output:
![Image](https://github.com/user-attachments/assets/c2ac7e57-8857-497c-ad59-376a0b6261d2)
