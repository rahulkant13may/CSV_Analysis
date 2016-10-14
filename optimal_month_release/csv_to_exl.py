import csv
import xlwt

cnt = 0
exl  = xlwt.Workbook()

sheet1 = exl.add_sheet('sheet1')

sheet1.write(0,1,'title')
sheet1.write(0,2,'score')
sheet1.write(0,3,'release_month')
sheet1.write(0,4,'editors_choice')

with open('ign.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cnt = cnt + 1 
        sheet1.write(cnt,1,row['title'])
        sheet1.write(cnt,2,row['score'])
        sheet1.write(cnt,3,row['release_month'])
        sheet1.write(cnt,4,row['editors_choice'])
    exl.save('optimal_month.xls')    