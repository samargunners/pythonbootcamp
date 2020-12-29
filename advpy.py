import shutil

shutil.unpack_archive('/Users/samarpatel/Downloads/Complete-Python-3-Bootcamp-master/12-Advanced Python Modules/08-Advanced-Python-Module-Exercise/unzip_me_for_instructions.zip','/Users/samarpatel/Desktop/samar/Code/GitDesktop/pyhtonbootcamp','zip')

with open ('/Users/samarpatel/Desktop/samar/Code/GitDesktop/pyhtonbootcamp/extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)

import re

def search(file,pattern= r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')

    if re.search(r'\d{3}-\d{3}-\d{4}',f.read()):
        return re.search(r'\d{3}-\d{3}-\d{4}',f.read())
    else:
        return ''


import os

result = []

for folder, sub_folders, files in os.walk('/Users/samarpatel/Desktop/samar/Code/GitDesktop/pyhtonbootcamp/extracted_content'):
    for f in files:
        full_path = folder + '/' + f
        result.append(search(full_path))

for r in result:
    if r != '':
        print(r.group())
