import os
import shutil

print(os.getcwd())
path = "C:\\Users\\DELL\\Downloads"
print(os.path.exists(path))

source = "C:\\Users\\DELL\\Downloads\\PROJECTS-MODULE-3\\project-99\\folder\\"
destination = "C:\\Users\\DELL\\Downloads\\MODULE-3\\folder2\\"

reading_files = os.listdir(source)
print(reading_files)


for file in reading_files:
    shutil.copy((source+file),destination)