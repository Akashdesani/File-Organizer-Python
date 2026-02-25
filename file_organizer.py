import os
import shutil

print("===== File Organizer =====")

path = input("Enter Folder Path: ")

images = [".jpg",".png",".jpeg"]
docs = [".pdf",".docx",".txt"]
videos = [".mp4",".mkv"]
programs = [".exe",".py"]

os.makedirs(path+"/Images",exist_ok=True)
os.makedirs(path+"/Documents",exist_ok=True)
os.makedirs(path+"/Videos",exist_ok=True)
os.makedirs(path+"/Programs",exist_ok=True)

files = os.listdir(path)

for file in files:

    file_path = path+"/"+file

    if os.path.isfile(file_path):

        ext=os.path.splitext(file)[1]

        if ext in images:

            shutil.move(file_path,path+"/Images/"+file)

        elif ext in docs:

            shutil.move(file_path,path+"/Documents/"+file)

        elif ext in videos:

            shutil.move(file_path,path+"/Videos/"+file)

        elif ext in programs:

            shutil.move(file_path,path+"/Programs/"+file)

print("Files Organized Successfully")