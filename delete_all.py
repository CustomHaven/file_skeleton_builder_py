import os

def check_dir(directory):
    return os.path.isdir(directory)

def delete_file(root, file):
    os.remove(os.path.join(root, file))

def delete_directory_and_contents(directory):
    if check_dir(directory) == False:
        return
    for root, dirs, files in os.walk(directory, topdown=False):  # Walk through directories bottom-up
        for file in files:
            delete_file(root, file)
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(directory)

all_dirs = os.listdir(".")

excluded_files = ["main.py", "delete_all.py", "create_all.py", "README.md"]
excluded_extensions = [".json", ".git", ".gitignore"]

items_to_delete = [item for item in all_dirs if item not in excluded_files and not any(item.endswith(ext) for ext in excluded_extensions)]

for item in items_to_delete:
    if check_dir(item):
        delete_directory_and_contents(item)
    else:
        delete_file(os.getcwd(), item)