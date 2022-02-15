import os

print(f"Your Whole file path is {os.getcwd()}")

file_path = os.getcwd()
# Gets entire filepath of current working directory

folder_name = os.path.basename(file_path)
# Gets folder name from filepath found above.

print(f"Your directory name is {folder_name}")
