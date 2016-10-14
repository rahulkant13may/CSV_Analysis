import xlrd 
import csv
import itertools
from collections import Counter
file_location = "award.xls"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)

cnt = 0

total = 0

for row in range(sheet.nrows):
    if sheet.cell_value(row,1) == 'Macintosh':
        cnt= cnt+1
        total = total + float(sheet.cell_value(row,2))

ans = total/cnt
print(ans)
