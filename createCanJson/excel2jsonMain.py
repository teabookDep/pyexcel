from excel_to_json import excel_to_json
from validate_json import is_json


SOURCESHEET = './caninfo.xlsx'
JSONFILE = './canlabel.json'


def write_json_file(json_data, filename):
    print('[-] Writing file...')
    output = open(filename, 'w')
    output.writelines(json_data)

    
def main():
    write_json_file(excel_to_json(SOURCESHEET), JSONFILE)
    print('[-] Validating json file...')
    print('Debug: ' + JSONFILE)
    if(is_json(JSONFILE)):
        print('[!] Successfully generated an updated dataset.')
    else:
        print('[!] Unable to validate json datafile, please review the sourcesheet and output.')
main()
