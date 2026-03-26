import os

# Specify the directory path
directory_path = "C:\\"  # Change this to your folder path

# List all files and folders in the directory
contents = os.listdir(directory_path)

# Print each item
print("Contents of the directory:")
for item in contents:
    print(item)