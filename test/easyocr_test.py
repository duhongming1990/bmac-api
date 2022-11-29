__author__ = 'duhongming'

import easyocr

# https://www.jaided.ai/easyocr/
reader = easyocr.Reader(['en'], model_storage_directory='../model/')
result = reader.readtext('easyocr_test.png')
print("".join(result[0][1].split(' ')))
