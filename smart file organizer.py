import os
import shutil
source = r"C:\Users\batra\Downloads\project folder\download"
os.makedirs("images" , exist_ok=True)
os.makedirs("pdfs", exist_ok=True)
os.makedirs("documents", exist_ok=True)
for files in os.listdir(source):
    filepath = os.path.join(source,files)
    if os.path.isfile(filepath):
        if files.endswith((".jpg",".jpeg",".png")):
            shutil.move(filepath,"images")
        elif files.endswith(".pdf"):
            shutil.move(filepath,"pdfs")
        elif files.endswith(".exe"):
            shutil.move(filepath,"documents")

