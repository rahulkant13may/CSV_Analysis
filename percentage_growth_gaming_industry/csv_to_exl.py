import csv 
import xlwt

cnt = 0
exl = xlwt.Workbook()

sheet1 = exl.add_sheet("sheet1")

sheet1.write(0,1,'title')
sheet1.write(0,2,'release_year')

with open('ign.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cnt = cnt + 1 
        sheet1.write(cnt,1,row['title'])
        sheet1.write(cnt,2,row['release_year'])
    exl.save('growth.xls')    