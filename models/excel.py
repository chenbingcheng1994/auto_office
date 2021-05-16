# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
from xlrd import open_workbook

#打开excel文件
with open_workbook('test.xls') as workbook:
    worksheet=workbook.sheet_by_name('first_sheet')
    for row_index in range(worksheet.nrows):
        for col_index in range(worksheet.ncols):
            print(worksheet.ncol)



#if __name__== '__main__':
#    sheet = open_excel()
#    print(sheet)
