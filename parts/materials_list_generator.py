import xlsxwriter
import datetime


def generate_materials_list(job_info,fixture_info):
    # workbook = xlsxwriter.Workbook(fr'/Users/paulwilliams/Work/test_folder/{job_info['builder'].upper()}/MATERIAL LIST/{job_info['plan'].upper()}.xlsx')
    # workbook = xlsxwriter.Workbook(fr'C:\Users\Paul.Williams\Stancil Services\Quan Estimating - Documents\General\{job_info['builder'].upper()}\QUOTES\{job_info['plan'].upper()}.xlsx')
    workbook = xlsxwriter.Workbook(fr'C:\Users\Paul.Williams\OneDrive - Stancil Services\Documents\Projects\TEST\NEW RES\{fixture_info['name'].upper()}\{job_info['plan'].upper()}.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.set_column('A:A',3)
    worksheet.set_column('B:B',22.71)
    worksheet.set_column('C:C',24.29)
    worksheet.set_column('D:D',37.86)
    worksheet.set_column('E:E',22.86)

    # cell formats
    bold = workbook.add_format({'bold':True})

    builder_title = workbook.add_format({'bold':True})
    builder_title.set_font_size(20)
    builder_title.set_align('center')


    title_row = workbook.add_format({'bold':True})
    title_row.set_font_size(18)
    title_row.set_align('center')

    # 
    worksheet.write('E5','Job Code', bold)
    worksheet.write('E6','DRCRS1085')

    # column headers
    worksheet.write('A7','PO#',title_row)
    worksheet.write('B7','Model #',title_row)
    worksheet.write('C7','UPC',title_row)
    worksheet.write('D7','Description',title_row)
    worksheet.write('E7','Order Qty',title_row)

    # 

    workbook.close()

    # Builder
    print(f'material_list_generator {job_info['builder']}')

    # Community
    print(f'material_list_generator {job_info['community']}')

    # Plan
    print(f'material_list_generator {job_info['plan']}')

    # PO number
    print(f'material_list_generator {job_info['po_number']}\n')
