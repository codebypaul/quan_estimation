import xlsxwriter

def list_generator(workbook,bath_count):
    worksheet = workbook.add_worksheet('Material List')

    worksheet.set_column('A:A',10)

    worksheet.write('A1',bath_count)