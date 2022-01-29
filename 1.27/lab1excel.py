import xlrd
import xlutils
from xlutils.copy import copy

book = xlrd.open_workbook('E:/Python/2022winter/1.27/test1.xls')
sheet1 = book.sheets()[0]
nrows = sheet1.nrows
print('表格总行数', nrows)
ncols = sheet1.ncols
print('表格总列数', ncols)
row3_values = sheet1.row_values(2)
print('第3行值', row3_values)
col3_values = sheet1.col_values(2)
print('第3列值', col3_values)
cell_3_3 = sheet1.cell(2, 2).value
print('第3行第3列的单元格的值:', cell_3_3)

# for i in range(nrows):
#     for j in range(ncols):
#         print(sheet1.cell(i, j))
def output():
    for i in range(nrows):
        print(sheet1.row_values(i))

def modify(row1, col1, newValue):
    wb = copy(book)
    ws = wb.get_sheet(0)
    ws.write(row1, col1, newValue)

modify(1, 1, "hh")
output()
