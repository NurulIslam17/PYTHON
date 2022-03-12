
from pathlib import Path
# absolute path > file from the hard disk
 #C:\Program Files\Microsoft

# Relatives path > file from the project packages

path=Path("ecomerce")
print(path.exists())

for file in (path.glob('*')):
    print(file)