import xlsxwriter
from test_quote import quote_generator
from test_material_list import list_generator

bath_count = 0

def collect_info():
    global bath_count
    bath_count = int(input('How many bathrooms are in this homes?\n'))

workbook = xlsxwriter.Workbook(fr'C:\Users\Paul.Williams\OneDrive - Stancil Services\Documents\Projects\TEST\Test_Book.xlsx')



collect_info()
job_info = {
    'community':community,
    'plan':project_name,
}
fixture_info = {}
floors = {}
bathrooms = {}


def create_document(workbook,bath_count,job_info,fixture_info,floors,bathrooms):
    # create the excel quote
    quote_generator(workbook,bath_count,job_info,fixture_info,floors,bathrooms)
    # create the excel materials list
    list_generator(workbook,bath_count)
    workbook.close()

create_document(workbook,bath_count,job_info,fixture_info,floors,bath_count,bathrooms)


# job_info,fixture_info,floors,bath_count,bathrooms