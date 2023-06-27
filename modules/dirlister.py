import os

def run(**args):
    print("[*] In dirlister module.")
    files=os.listdir(".")   #得到当前文件夹下的所有子项名
    return str(files)

