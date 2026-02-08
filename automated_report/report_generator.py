import csv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# File names
DATA_FILE = "data.csv"
PDF_FILE = "report.pdf"

# Read CSV data
names = []
marks = []

with open(DATA_FILE, "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        names.append(row[0])
        marks.append(int(row[1]))

# Data analysis
total_students = len(marks)
average_marks = sum(marks) / total_students
highest_marks = max(marks)
lowest_marks = min(marks)

# Create PDF
c = canvas.Canvas(PDF_FILE, pagesize=A4)
width, height = A4

# Title
c.setFont("Helvetica-Bold", 18)
c.drawString(180, height - 50, "Student Marks Report")

# Summary
c.setFont("Helvetica", 12)
y = height - 100

c.drawString(50, y, f"Total Students: {total_students}")
y -= 20
c.drawString(50, y, f"Average Marks: {average_marks:.2f}")
y -= 20
c.drawString(50, y, f"Highest Marks: {highest_marks}")
y -= 20
c.drawString(50, y, f"Lowest Marks: {lowest_marks}")

# Table header
y -= 40
c.setFont("Helvetica-Bold", 12)
c.drawString(50, y, "Name")
c.drawString(300, y, "Marks")

# Table data
c.setFont("Helvetica", 12)
y -= 20

for i in range(total_students):
    c.drawString(50, y, names[i])
    c.drawString(300, y, str(marks[i]))
    y -= 20

# Save PDF
c.save()
print("PDF report generated successfully!")
