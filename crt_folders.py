#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 批量新建文件夹

import os

filename="folders.txt"

def create_folder(path_str):
    try:
        print(path_str.strip())
        os.makedirs(path_str.strip())
    except Exception as e:
        print(e)

with open(filename,"r",encoding="utf-8") as f:    
    n = 1
    while True:
        line = f.readline()
        # EOF exit
        if not line:
            break
        # create folder
        print(n, end=":")
        create_folder(line)
        n = n + 1

print("\n{} folders is created!".format(n-1))

    
