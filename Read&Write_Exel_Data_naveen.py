__author__ = "Naveen kumar"

import xlwt
from xlwt import Workbook
from datetime import date
import time

def naveen(path):
    ledgeer_book = Workbook()

    my_sheet = ledgeer_book.add_sheet("my_sheet")
    they_sheet = ledgeer_book.add_sheet("they_sheet")
    our_sheet = ledgeer_book.add_sheet("our_sheet")
    total_sheet = ledgeer_book.add_sheet("total_sheet")

    colums = ["x","y","z","j","t"]
    txt = "Row %s, Col %s"

    for num in range(4):
        row = my_sheet.row(num)
        for index, col in enumerate(colums):
            value = txt % (num +1,col)
            row.write(index,value)



    naveen_dob = date(1999,11,9)
    current_time = time.ctime()
    value ="Pawan kalyan"
    married_dob = date(1995,2,28)
    fmt = xlwt.Style.easyxf("""
    font: name Arial;
    borders: left thick,right thick,top thick,bottom thick;
    pattern: pattern solid,fore_colour pink;
    """,num_format_str ="YYYY-MM_DD")
    my_sheet.write(7,3,naveen_dob,fmt)
    they_sheet.write(4,2,current_time,fmt)
    our_sheet.write(1,8,value,fmt)
    total_sheet.write(2,6,married_dob,fmt)

    ledgeer_book.save("aiii.xls")



# if __name__ == "--main--":
#    path = r"aiii.xls"
#    naveen(path)


# """
# Here we use a large string to specify to xlwt that we want to apply a style that uses the Arial font, has borders on all four sides of the cell and the fore_color is red. When you execute the code, you will find that fore_color actually means background color. Anyway, this syntax makes it very easy to style a cell’s contents. There are a lot of good examples in this PDF that the Python Excel website put out.
# """

import xlrd
from xlrd import open_workbook



def praveen(path):
    """
    Open and read an Excel file
    """
    # book = xlrd.open_workbook(path)
    book = open_workbook(path)
    # print number of sheets
    # print(book.nsheets)
    # print sheet names
    # print(book.sheet_names())

    # get the first worksheet based on index
    # first_sheet = book.sheet_by_index(0)
    first_sheet = book.sheet_by_name("my_sheet")
    # can get the row based valuesyy

    print(first_sheet.row_values(7,3))

    # can get the colum based values
    # print(first_sheet.col_values(2))
    # read a cell
    # second_sheet = book.sheet_by_index(1)
    # value = second_sheet.cell_value(4,2)
    # print(value)

    sheet_2 = book.sheet_by_name("they_sheet")
    print(sheet_2.row_values(4,2))

    x = first_sheet.cell_value(2,2)
    print(x)
    sheet_3 = book.sheet_by_name("our_sheet")
    # sheet_3 = book.sheet_by_index(2)

    print(sheet_3.row_values(1,8))
    print(sheet_3.col_values(1,8))


    sheet_3 = book.sheet_by_name("total_sheet")
    sheet_3 = book.sheet_by_index(4)

    print(sheet_3.row_values(2,6))
    print(sheet_3.col_values(2,6))

    sheet_5 = book.sheet_by_index(4)
    language = sheet_5.cell_value(2,2)
    print(language)



# if __name__ == "__main__":
    path = r"aiii.xls"
    praveen(path)





# following link for reading data from the excel
# https://www.blog.pythonlibrary.org/2014/04/30/reading-excel-spreadsheets-with-python-and-xlrd/




