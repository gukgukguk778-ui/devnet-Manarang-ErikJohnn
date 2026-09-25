"""
Module 2 — Activity: File Sorting with os and shutil
Student: Erik John D. Manarang
Date: 9/25/26

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I made a Python script that automatically makes a compressed zip backup of my project directory. The script makes a file name that has todays exact date and time so that older backups are never overwritten. Then the script puts the zip archive into a Backups" folder automatically.


============================================
KEY VOCABULARY
============================================
- os module: A built in Python tool used to interact with computer folders and files.
- shutil module: to use this when i need move/copy my files.
- file path: this tells python where a file is located.
- directory: this is essentially a folder where files are stored.
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil


main_folder = "School_Work"
subjects = ["Math", "Science", "English", "History", "Art"]

for subject in subjects:
    folder_path = os.path.join(main_folder, subject)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created folder for: {subject}")

print("All subject folders created successfully!")



"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I want to avoid is forgetting to add 'exist_ok=True', inside 'os.makedirs()'. If I don’t include it and I run the program again and the folders are already there Python will crash with an error. Adding 'exist_ok=True' tells Python to not try to create the folder if it already exists. It just skips that step so the program keeps running without issues. This small detail helps avoid errors and makes the code more reliable.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
