#Python code to organize folders in computer

import os
import shutil

#Example: create a folder on Desktop to test the functionality.

path = '../../Desktop/test_folder'

file_names = os.listdir(path)

#Create destination folders for the files inside the path

folder_mappings:{
        ".png": "Images",
        ".svg": "Vector files",
        ".tgz": "TAR files",
        }

for folder_name in set(folder_mappings.values())
    folder_path = os.path.join(path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_name}")


