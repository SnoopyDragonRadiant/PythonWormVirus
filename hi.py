import shutil
import os

opt = bool(int(input("Do you want to infect or clear[1/0]: ")))
dir_name = str(input("What do you want the directory to be called: "))
main_path= os.getcwd()
print(f"{main_path}\\{dir_name}")

n = 0
if opt:
    src = f"{main_path}\\tiki.txt"

    while True:
        if os.path.isdir(f"{main_path}\\{dir_name}"):
            dest = f"{main_path}\\{dir_name}\\tiki{n}.txt"
        else:
            os.mkdir(dir_name)
            dest = f"{main_path}\\{dir_name}\\tiki{n}.txt"
        shutil.copy(src=src,dst=dest)
        print(f"Copied {n}")
        n+=1
elif not opt:
    shutil.rmtree(f"{main_path}\\{dir_name}")