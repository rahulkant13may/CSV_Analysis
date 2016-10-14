import csv 
import xlrd


list = {}
from collections import Counter
file_location = 'optimal_month.xls'

workbook = xlrd.open_workbook(file_location)

sheet = workbook.sheet_by_index(0)

jan,feb ,mar,apr, may, jun , july , aug , sep, october, nov, dec = 0,0,0,0,0,0,0,0,0,0,0,0, ;
#jan = 0, feb = 0, mar = 0,apr = 0, may = 0, jun = 0, july = 0, aug = 0, sep= 0, october = 0,  nov = 0, dec = 0 ;
#jan_cnt = 0, feb_cnt = 0, mar_cnt = 0,apr_cnt = 0, may_cnt = 0, jun_cnt = 0, july_cnt = 0, aug_cnt = 0, sep_cnt =0; octo_cnt = 0, nov_cnt = 0, dec_cnt = 0 ;
jan_cnt , feb_cnt, mar_cnt,apr_cnt , may_cnt , jun_cnt , july_cnt , aug_cnt , sep_cnt , october_cnt , nov_cnt ,dec_cnt = 0,0,0,0,0,0,0,0,0,0,0,0 ;
#
#hola = 0 ;
#hola_cnt = 0 ;
#jan = 0 ;
#jan_cnt = 0 ;

for row in range(sheet.nrows):
#    print("Hi")
#    if (sheet.cell_value(row,4) == 'Y') and (sheet.cell_value(row,3) == 13):
##        print("heloo")
#        hola_cnt = hola_cnt + 1
#        hola = hola + float(sheet.cell_value(row,2))   
#        print(sheet.cell_value(row,1))
        
    if (sheet.cell_value(row,4) == 'Y') and (sheet.cell_value(row,3) == '1'):
        jan_cnt = jan_cnt + 1
        jan = jan + float(sheet.cell_value(row,2))
#        print("jan")
#        print(sheet.cell_value(row,1))
        
    elif (sheet.cell_value(row,4) == 'Y') and (sheet.cell_value(row,3) == '2'):
        
        feb_cnt = feb_cnt + 1 
        feb = feb + float(sheet.cell_value(row,2))

    elif (sheet.cell_value(row,4) == 'Y') and (sheet.cell_value(row,3) == '3'):
        mar_cnt = mar_cnt + 1 
        mar = mar + float(sheet.cell_value(row,2))

    elif (sheet.cell_value(row,4) == 'Y') and (sheet.cell_value(row,3) == '4'):
        apr_cnt = apr_cnt + 1 
        apr = apr + float(sheet.cell_value(row,2))

    elif (sheet.cell_value(row,4) == 'Y') and (sheet.cell_value(row,3) == '5'):
        may_cnt = may_cnt + 1
        may = may + float(sheet.cell_value(row,2))

    elif (sheet.cell_value(row,4) == 'Y') and (sheet.cell_value(row,3) == '6'):
        jun_cnt = jun_cnt + 1
        jun = jun + float(sheet.cell_value(row,2))

    elif (sheet.cell_value(row,4) == 'Y') and (sheet.cell_value(row,3) == '7'):
        july_cnt = july_cnt + 1 
        july = july + float(sheet.cell_value(row,2))

    elif (sheet.cell_value(row,4) == 'Y') and (sheet.cell_value(row,3) == '8'):
        aug_cnt = aug_cnt + 1
        aug = aug + float(sheet.cell_value(row,2))

    elif (sheet.cell_value(row,4) == 'Y') and (sheet.cell_value(row,3) == '9'):
        sep_cnt = sep_cnt + 1
        sep = sep + float(sheet.cell_value(row,2))

    elif (sheet.cell_value(row,4) == 'Y') and (sheet.cell_value(row,3) == '10'):
        october_cnt = october_cnt + 1
        october = october + float(sheet.cell_value(row,2))

    elif (sheet.cell_value(row,4) == 'Y') and (sheet.cell_value(row,3) == '11'):
        nov_cnt = nov_cnt + 1
        nov = nov + float(sheet.cell_value(row,2))
#        print("nov")
#        print(sheet.cell_value(row,1))

#     if sheet.cell_value(row,3) == '13':
#        hola_cnt = hola_cnt + 1
#        hola = hola + float(sheet.cell_value(row,2))   
#        print(sheet.cell_value(row,1))
##            
    elif (sheet.cell_value(row,4) == 'Y') and (sheet.cell_value(row,3) == '12'):
        dec_cnt = dec_cnt + 1

        dec = dec + float(sheet.cell_value(row,2))    

        
list["jan"] = jan/jan_cnt
list["feb"] = feb/feb_cnt
list["mar"] = mar/mar_cnt
list["apr"] = apr/apr_cnt
list["may"] = may/may_cnt
list["jun"] = jun/jun_cnt
list["july"] = july/july_cnt
list["aug"] = aug/aug_cnt
list["sep"] = sep/sep_cnt
list["october"] = october/october_cnt
list["nov"] = nov/nov_cnt
list["dec"] = dec/dec_cnt

print(list)

print(max(list, key=list.get))

        
        
        
        
        
        
        
        
        
        
#        
#print(hola)
#print(hola_cnt)
#

#
#print("jan avg" )
#list.append(jan/jan_cnt)
#
#print("feb avg")
#list.append(feb/feb_cnt)
#
#print("mar avg")
#list.append(mar/mar_cnt)
#
#print("apr avg")
#list.append(apr/apr_cnt)
#
#print("may avg")
#list.append(mar/mar_cnt)
#
#
#print("jun avg")
#list.append(jun/jun_cnt)
#
#print("july avg")
#list.append(july/july_cnt)
#
#print("aug avg")
#list.append(aug/aug_cnt)
#
#print("sep avg")
#list.append(sep/sep_cnt)
#
#print("oct avg")
#list.append(october/october_cnt)
#
#
#print("nov avg ")
#list.append(nov/nov_cnt)
#
#print("Dec avg")
#list.append(dec/dec_cnt)
#        
#print(max(list))       
    
    
    
    
    
    
 
