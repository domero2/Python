from os import listdir
from os.path import isfile, join

def DeleteUnnecessaryScript(LookingforArgument,path_to_folder):
    path = path_to_folder
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for file in onlyfiles:
        with open(path_to_folder+file, 'r+') as open_file:
            content = open_file.readlines()
            try:
                if content.index(LookingforArgument):
                    del content[content.index(LookingforArgument):content.index(content[-1])+1]
            except ValueError:
                pass
            open_file.close()
            with open(os.path.join('/Users/amajcher/Desktop/Python/returns/{}'.format(file)), 'w+') as write_file:
                write_file.write(''.join(content))
                write_file.close()
DeleteUnnecessaryScript(' IN (\n','/Users/amajcher/Desktop/Python/replace/')

def GenerateFinalFiles(path_to_files):
    path = path_to_files
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for i in onlyfiles:
        with open(path_to_files+i, "a+") as file:
            file.write(f'''create or replace TABLE "TestTable{i}"(
    "SFirstColumn" CHAR );''')
    file.close()

GenerateFinalFiles('/Users/amajcher/Desktop/Python/returns/')