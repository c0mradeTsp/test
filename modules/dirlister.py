import os

def rub(**args):
    print("[*] In dirlister module.")
    files=os.listdir(".")   #�õ���ǰ�ļ����µ���������
    return str(files)