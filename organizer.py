import os
import shutil

source = "Downloads"

for file in os.listdir(source):

    filepath = os.path.join(source, file)

    if os.path.isfile(filepath):

        if file.endswith(".jpg"):
            shutil.move(filepath, "Images/" + file)

        elif file.endswith(".pdf"):
            shutil.move(filepath, "PDFs/" + file)

        elif file.endswith(".mp4"):
            shutil.move(filepath, "Videos/" + file)





    

    


