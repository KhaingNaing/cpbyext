import sys
from pathlib import Path
import os
import shutil
import tempfile
from zipfile import ZipFile
def main():
    args = sys.argv[1:]
    if args == []:
        print('Usage: python3 cpbyext.py <ext1> <ext2> ...')
        sys.exit(1)

    # Counter for files copy
    total_file_count = int()
    
    # Set path to the current directory 
    path = Path(".")
    temp_dir = tempfile.mkdtemp()

    for ext in args:
        file_count = 0
        file_list = list(path.rglob("*." + ext))

        if not file_list:
            print(f"NO {ext.upper()} FILES TO COPY")
            continue

        for file in file_list:
            f_path = Path(file)
            shutil.copy(f_path, temp_dir)
            file_count+=1
        print(f"Copied {file_count} {ext.upper()} files")
        total_file_count += file_count


    zip_file_name = 'cpfiles.zip'
    with ZipFile(zip_file_name, 'w') as myzip:
        for root, dirnames, filenames in os.walk(temp_dir):
            for file in filenames:
                file_path = Path(root) / file                        
                arcname = os.path.relpath(file_path, start=temp_dir)
                myzip.write(file_path, arcname=arcname)

    shutil.rmtree(temp_dir)
    if total_file_count > 0:
        print(f"Total {total_file_count} files copied and zipped into {zip_file_name}.")
    else:
        print("No files were copied.")

if __name__ == "__main__":
    main()
