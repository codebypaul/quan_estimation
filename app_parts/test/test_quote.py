import xlsxwriter
import datetime

def quote_generator(workbook,bath_count):
    worksheet = workbook.add_worksheet('Quote')

    # format worksheet
    worksheet.set_column('A:A',3)
    worksheet.set_column('B:B',5.56)
    worksheet.set_column('C:C',51.36)
    worksheet.set_column('D:D',10)
    worksheet.set_column('E:E',10)

    # cell formats
    bold = workbook.add_format({'bold':True})

    builder_title = workbook.add_format({'bold':True})
    builder_title.set_font_size(20)
    builder_title.set_align('center')

    community_title = workbook.add_format({'bold':True})
    community_title.set_font_size(16)
    community_title.set_align('center')

    project_title = workbook.add_format({'bold':True})
    project_title.set_font_size(14)
    project_title.set_align('center')

    room_title = workbook.add_format({'bold':True})

    color_title = workbook.add_format({'bold':True})
    color_title.set_align('center')

    quantity = workbook.add_format()
    quantity.set_align('center')

    num_format = workbook.add_format()
    num_format.set_num_format('#,##0.00')

    sub_item = workbook.add_format()
    sub_item.set_indent(3)

    tap_depth = workbook.add_format({'bold':True})
    tap_depth.set_indent(6)

    total_price_format = workbook.add_format({'bold':True})
    total_price_format.set_font_size(16)
    total_price_format.set_align('center')

    # builder
    # worksheet.write('C1',fixture_info['name'].upper(),builder_title)
    # community
    # worksheet.write('C2',job_info['community'].upper(),community_title)
    # project
    # worksheet.write('C3',job_info['plan'].upper(),project_title)
    # date
    # worksheet.write('B5',today)

    worksheet.write('D5','PRICE')
    worksheet.write('E5','EXTENDED')