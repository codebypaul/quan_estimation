import xlsxwriter
import datetime


def generate_materials_list(job_info,fixture_info):
    workbook = xlsxwriter.Workbook(fr'/Users/paulwilliams/Work/test_folder/{job_info['builder'].upper()}/MATERIAL LIST/{job_info['plan'].upper()}.xlsx')
    # workbook = xlsxwriter.Workbook(fr'C:\Users\Paul.Williams\Stancil Services\Quan Estimating - Documents\General\{job_info['builder'].upper()}\QUOTES\{job_info['plan'].upper()}.xlsx')
    worksheet = workbook.add_worksheet()

    # cell formats

    builder_title = workbook.add_format({'bold':True})
    builder_title.set_font_size(20)
    builder_title.set_align('center')

    workbook.close()

    # Builder
    print(f'material_list_generator {job_info['builder']}')

    # Community
    print(f'material_list_generator {job_info['community']}')

    # Plan
    print(f'material_list_generator {job_info['plan']}')

    # PO number
    print(f'material_list_generator {job_info['po_number']}\n')
