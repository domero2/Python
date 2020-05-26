from contextlib import contextmanager
from os import path
BASE_PATH = path.dirname(path.abspath(__file__))

# with open('file.txt', 'w') as file_one:
#     file_one.write('test')
#     file_one.close()

class File:
    def __init__(self,filename,method):
        self.file = open(filename,method)

    def __enter__(self):
        print('Enter')
        return self.file

    def __exit__(self, type, value, traceback):
        print(f"{type},{value},{traceback}")
        print('Exit')
        self.file.close()
        # handle Exception error inside exit method
        if type == Exception:
            return True

with File(BASE_PATH+"/file2.txt", "w") as f:
    print('mid')
    f.write('hi')
    raise Exception()

print('\n\n --------')

#decorate context manager
@contextmanager
def file_o(filename, method):
    print('enter')
    file = open(filename, method)
    yield file
    file.close()
    print('exit')

with file_o(BASE_PATH+"/text.txt", "w") as f:
    print('mid')
    f.write('hello')