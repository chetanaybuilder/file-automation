import os
import shutil
import schedule
import time

source = "."

def organize_files():

    for file in os.listdir(source):

        if file.endswith(".jpg"):
            os.makedirs("images", exist_ok=True)
            shutil.move(file, "images")

        elif file.endswith(".pdf"):
            os.makedirs("pdfs", exist_ok=True)
            shutil.move(file, "pdfs")

        elif file.endswith(".exe"):
            os.makedirs("software", exist_ok=True)
            shutil.move(file, "software")

    print("Files organized successfully!")

# Run every day at 9 PM
schedule.every().day.at("21:00").do(organize_files)

print("Smart File Organizer is running...")

while True:
    schedule.run_pending()
    time.sleep(1)
                    

        



