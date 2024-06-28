import xlsxwriter
from test_quote import quote_generator
from test_material_list import list_generator

bath_count = 0

def collect_info():
    global bath_count
    bath_count = int(input('How many bathrooms are in this homes?\n'))

workbook = xlsxwriter.Workbook(fr'C:\Users\Paul.Williams\OneDrive - Stancil Services\Documents\Projects\TEST\Test_Book.xlsx')

def create_document(workbook,bath_count):
    quote_generator(workbook,bath_count)
    list_generator(workbook,bath_count)
    workbook.close()

collect_info()
print(bath_count)
create_document(workbook,bath_count)
