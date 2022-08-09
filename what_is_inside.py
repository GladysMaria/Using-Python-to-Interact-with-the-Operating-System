""" Checks what is inside a directory (subdirectories and files). """

import os

dir = 'file_path' # On Windows absolute path works by adding double slash.
name_list = os.listdir(dir) # Make a list with subdirectories and files inside of dir.

for name in name_list:
    fullname = os.path.join(dir, name) # Join path components intelligently.
    if os.path.isdir(fullname):
        print(f'{fullname} is a directory')
    else:
        print(f'{fullname} is a file')
