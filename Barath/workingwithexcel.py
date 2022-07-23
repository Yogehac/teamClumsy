import xlrd

loc = (r"C:\Users\bhara\PycharmProjects\KothariSugars\internship\Copy of KOTHARISTRUCTxlsx.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
# print(sheet)
# for rx in range(18,49):
#     print(sheet.row(rx))
print(sheet.row_values(22))
print(type(sheet))
