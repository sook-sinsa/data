import xlrd
from collections import OrderedDict
import json

file = "datasheet.xls"

wb = xlrd.open_workbook(file)
sh = wb.sheet_by_index(0)

data_list = []

for row in range(1, sh.nrows):
    data = OrderedDict()
    row_values = sh.row_values(row)
    data['bigCatNum'] = row_values[0]
    data['smallCatNum'] = row_values[1]
    data['productNum'] = row_values[2]
    data['category'] = row_values[3]
    data['color'] = row_values[4]
    data['url'] = row_values[5]
    data_list.append(data)

j = json.dumps(data_list, ensure_ascii=False)

with open('datasheet.json', 'w+') as f:
    f.write(j)