def generate_options_list():
    workbook = xlsxwriter.Workbook(fr'C:\Users\Paul.Williams\Stancil Services\Quan Estimating - Documents\General\{fixture_info['name'].upper()}\QUOTES\{job_info['plan'].upper()}.xlsx')
    worksheet = workbook.add_worksheet()

    #format columns
    worksheet.set_column('A:A',10.11)
    worksheet.set_column('B:B',11.22)
    worksheet.set_column('C:C',16.22)
    worksheet.set_column('D:D',14.67)
    worksheet.set_column('E:E',29.11)
    worksheet.set_column('F:F',7.22)
    worksheet.set_column('G:G',11.22)
    worksheet.set_column('H:H',9.11)