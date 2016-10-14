import csv
import xlrd
import pandas as pd
import numpy as np
from collections import Counter,OrderedDict

list = []
row = 1
file_loacation = 'growth.xls'

workbook = xlrd.open_workbook(file_loacation)

sheet1 = workbook.sheet_by_index(0)

for row in range(sheet1.nrows)[1:]:
    list.append(sheet1.cell_value(row,2))
    
c = Counter(list)

dictionary = dict(c)

#dictionary = {'carl':40,
#          'alan':2,
#          'bob':1,
#          'danny':3}
#order = OrderedDict(sorted(dict(c).items(), key=lambda t: t[0]))

#print(order)
print(dictionary)
#print(c)
#print(sorted(dict(c)).items())

keylist = dictionary.keys()
#
for key in sorted(keylist):
    print ("%s: %s" % (key, dictionary[key]))
    
    

#sortedlist = [1,149,205,339,775,1045,688,936,969,997,1088,1208,1610,1915,1687,1363,1073,753,696,537,365,226]    
    
#prices = [30.4, 32.5, 31.7, 31.2, 32.7, 34.1, 35.8, 37.8, 36.3, 36.3, 35.6]

#price_series = pd.Series(dictionary.values())
#print(price_series.pct_change())

#print(price_series.pct_change())    
#print(sorted(dictionary.values()))    
#
#
#price_series = pd.Series(prices)
#price_series.pct_change()
#import numpy as np
#a = np.array(sortedlist, dtype=float)
a = np.array(sorted(dictionary.values()), dtype=float)
#np.diff(a) / a[:-1] * 100
#
#a = np.array()
#
#np.diff(a) / a[:-1] * 100
print(np.diff(a) / a[:-1] * 100)



    