#Python code to organize folders in computer

import os
import shutil

#Example: create a folder on Desktop to test the functionality.

path = '../../Desktop/test_folder'

file_names = os.listdir(path)

#Create destination folders for the files inside the path

folder_mappings = {
        ".png": "Images",
        ".svg": "SVG files",
        ".tar.gz": "TAR files"
        }

for folder_name in set(folder_mappings.values()):
    folder_path = os.path.join(path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_name}")

for file_name in file_names:
    # Ignore folders and hidden files
    if os.path.isfile(os.path.join(path, file_name)):
        file_extension = os.path.splitext(file_name)[1].lower()

        if file_extension in folder_mappings:
            destination_folder_name = folder_mappings[file_extension]
            source_path = os.path.join(path, file_name)
            destination_path = os.path.join(path, destination_folder_name, file_name)
            print(f"Moving '{file_name}' to '{destination_folder_name}'...")
            shutil.move(source_path, destination_path)

print("Done! Your folder is now organized.")

