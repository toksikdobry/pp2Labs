import os
path = input()
folders = []
files = []
os.chdir(path)

dir = os.listdir(os.getcwd())
for i in dir:
    if os.path.isdir(i):
        folders.append(i)
    elif os.path.isfile(i):
        files.append(i)
print('Directories: ', *folders, sep = ", ")
print('Files: ',*files)
print('All: ')
for i in dir:
    if os.path.isdir(i):
        print(f'Directory {i}')
    elif os.path.isfile(i):
        print(f'File {i}')