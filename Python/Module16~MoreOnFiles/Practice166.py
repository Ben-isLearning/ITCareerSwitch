import shutil
import os

# Create new file. Write Lines of text to file.
# Copy to different name.
# Append lines to copied file.
# Print both files.

# Create New File
with open("BeefDemo.txt", "x") as mike:
    # Write Lines of Text
    for i in range(5):
        mike.write("I like beef!\n")

# Copy to New Name
src = "BeefDemo.txt"
dst = "BeefBeef.txt"

shutil.copy(src, dst)

# Append Copied File
with open("BeefBeef.txt", "a") as romeo:
    for i in range(5):
        romeo.write("I LOVE BEEF!\n")

# Print 1st file
with open("BeefDemo.txt", "r") as mike:
    print(mike.read())

# print 2nd file
with open("BeefBeef.txt", "r") as romeo:
    print(romeo.read())
