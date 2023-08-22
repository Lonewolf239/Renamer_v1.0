import os

print("|===========================|\n"
      "|  Renamer by. Lonewolf239  |\n"
      "|       VK: @1blitz01       |\n"
      "|===========================|\n")
folder_path = input("Enter the path to the folder in which you want to rename the files (example: C:\\test_folder)\n"
                    "Folder path: ")
files = os.listdir(folder_path)
files.sort()
for i, file_name in enumerate(files):
    file_name_without_extension, extension = os.path.splitext(file_name)
    new_file_name = f"{i + 1}{extension}"
    os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

input("\n\n|==============================|\n"
      "| The files have been renamed! |\n"
      "|    Press enter to exit...    |\n"
      "|==============================|\n\n")
