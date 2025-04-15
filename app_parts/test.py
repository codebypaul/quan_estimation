import xlsxwriter

workbook = xlsxwriter.Workbook(fr'C:\Users\paul.williams\OneDrive - Stancil Services\Documents\TEST\BUILDERS\RED CEDAR\QUOTES\Test.xlsx')
worksheet=workbook.add_worksheet('Sheet1')
worksheet.write('A1','Hello World!')
workbook.close()