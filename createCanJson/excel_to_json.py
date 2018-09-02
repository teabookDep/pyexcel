import simplejson as json
import xlrd
from collections import OrderedDict


def excel_to_json(filename):
    workbook = xlrd.open_workbook(filename)
    ransomware_sheet = workbook.sheet_by_index(0)

    # List to hold dictionaries
    c_list = []

    # Iterate through each row in worksheet and fetch values into dict
    for rownum in range(1, ransomware_sheet.nrows):
        wares = OrderedDict()
        ransomware_values = ransomware_sheet.row_values(rownum)

        wares['val1'] = ransomware_values[1]
        wares['val2'] = ransomware_values[2]
        wares['val3'] = ransomware_values[3]

        c_list.append(wares)

    # Serialize the list of dicts to JSON
    return json.dumps(c_list, indent=4)
