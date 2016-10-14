import csv
import xlwt
cnt = 0;
exl = xlwt.Workbook()
sheet1 = exl.add_sheet("sheet1")
sheet1.write(0,1,'platform')
sheet1.write(0,2,'editors_choice')
with open('ign.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cnt = cnt + 1;
        sheet1.write(cnt,1,row['platform'])
        sheet1.write(cnt,2,row['editors_choice'])
    exl.save('try3.xls')