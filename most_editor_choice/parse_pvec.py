import xlrd 
import csv
import itertools
from collections import Counter
file_location = "try3.xls"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
box = []

for row in range(sheet.nrows):
    if sheet.cell_value(row,2) == 'Y':
        box.append(sheet.cell_value(row,1))

#print(Counter(box))    
c = Counter(box)
print(c.most_common(1)[0][0])
