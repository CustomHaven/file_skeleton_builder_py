import os

def delete_file(root, file):
    os.remove(os.path.join(root, file))

def delete_directory_and_contents(directory):
    for root, dirs, files in os.walk(directory, topdown=False):  # Walk through directories bottom-up

        # Delete all files first
        for file in files:
            delete_file(root, file)  # Remove the file
        # Delete all empty subdirectories
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))  # Remove empty subdirectories
    # Now remove the main directory
    os.rmdir(directory)


all_dirs = os.listdir(".")

excluded_files = ["delete_all.py", "create_all.py"]
excluded_extensions = [".json", ".git", ".gitignore"]

items_to_delete = [item for item in all_dirs if item not in excluded_files and not any(item.endswith(ext) for ext in excluded_extensions)]

for item in items_to_delete:
    if os.path.isdir(item):
        delete_directory_and_contents(item)
    else:
        delete_file(os.getcwd(), item)