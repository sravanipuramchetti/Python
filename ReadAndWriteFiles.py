from openpyxl import Workbook

wb = Workbook()
sheet = wb.create_sheet("Sample")
wb.save(filename="D:\\sampleworkbook.xlsx")

