from pathlib import Path

# Prefixing a string with 'r' will make it a raw string and it will have no escape character so we can do away with double backslashes

# Path(r"C:\Program Files\Microsoft")
# Path() # current folder
# Path.home()  # home directory
#
# path = Path("ecommerce/__init__.py")
# print(path.exists())
# print(path.is_file())
# print(path.is_dir())
# print(path.name)  # full name of the file with extension
# print(path.stem)  # only name of the file excluding extension
# print(path.suffix)  # only the extension of the file
# print(path.parent)  # parent directory name
# print(path.absolute())
# path.with_name("file.txt")

# WORKING WITH DIRECTORIES

path = Path("Modules")
path.exists()
#path.mkdir()  # creates a new directory
#path.rmdir()  # removes the directory
# path.rename("modules")

paths = [p for p in path.iterdir() if p.is_file()]
py_files = [p for p in path.glob("*.py")]
print(paths)

from pathlib import Path
path = Path("test.txt")
print(path.absolute())
if path.exists():
    print("File exists")
    exit(10)
path.mkdir()
print(path.exists())
