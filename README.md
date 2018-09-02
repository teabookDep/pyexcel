
# Ransomware-Json-Dataset
Compiles a json dataset containing properties to aid in the detection and mitigation of over 400 variants of ransomware using public sources.

[![Build Status](https://travis-ci.org/codingo/Ransomware-Json-Dataset.svg?branch=master)](https://travis-ci.org/codingo/Ransomware-Json-Dataset)
[![License](https://img.shields.io/badge/license-GPL3-_red.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![Python 3.2|3.6](https://img.shields.io/badge/python-3.2|3.6-green.svg)](https://www.python.org/)
[![Twitter](https://img.shields.io/badge/twitter-@codingo__-blue.svg)](https://twitter.com/codingo_)


## Install Dependencies
```
pip install -r requirements.txt
```
## Run Updater
```
python ./createCanJson/excel2jsonMain.py
```

The latest version of the Ransomware Summary spreadsheet will then be downloaded and processed into a local json output which will be found in the core folder of your local repository along with a copy of the latest version of the spreadsheet. To change the source and destinations for local files edit the constants found in the header of the 'update_json.py' file.

## Attribution / Credits
JSON dataset work is based upon the Ransomware Summary public spreadsheet that is managed by the many efforts of Mosh (@nyxbone) and @cyb3rops and can be found at: http://goo.gl/b9R8DE. Spreadsheet data remains the intellectual property of Mosh and is taken 'as-is' and processed into a more programming friendly JSON output to allow its use in various shell or programming operations. Spreadsheet is cloned within this repository for redundancy purposes.
