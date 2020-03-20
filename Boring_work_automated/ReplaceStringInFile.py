import os
list_of_tables=[
"Table1",
"Table2",
"Table3"]

def generateFile(file_name):
    if os.path.isfile("/Users/amajcher/Desktop/Python/NewFiles/{file}".format(file=file_name)):
        print('{file}: This file exist in /Users/amajcher/Desktop/Python/NewFiles/'.format(file=file_name))
    else:
        with open( "/Users/amajcher/Desktop/Python/NewFiles/{file}".format(file=file_name), "w") as file:
            for i in list_of_tables:
                file.write(f'''
"table_name": "{i}"''')

def ReplaceFile(file_name,write_file):
    with open(os.path.join('/Users/amajcher/Desktop/Python/NewFiles/{}'.format(file_name)), 'r+') as file:
        contents = file.readlines()
        with open(os.path.join('/Users/amajcher/Desktop/Python/NewFiles/{}'.format(write_file)), 'w+') as file2:
            for i in contents:
                file2.write(i.replace(':','='))