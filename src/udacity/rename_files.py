__author__ = 'Lunding'
import os

def rename_files():
    file_list = os.listdir(r"/Users/Lunding/Downloads/prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"/Users/Lunding/Downloads/prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    print(file_list)
    os.chdir(saved_path)
rename_files()