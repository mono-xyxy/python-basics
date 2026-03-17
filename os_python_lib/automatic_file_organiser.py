import os
import shutil

path = "test_dir"

os.chdir(path)

files = os.listdir()

for file in files:
    if file.endswith(".jpg"):
        folder = "Images"
    elif file.endswith(".pdf"):
        folder = "Documents"
    elif file.endswith(".py"):
        folder = "Code"
    else:
        folder = "Others"
    
    if not os.path.exists(folder):
        os.mkdir(folder)

    shutil.move(file,os.path.join(folder,file))

print("Files Organised!")