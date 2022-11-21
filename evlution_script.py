# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 23:40:50 2022

@author: System Administrator
"""
#tesseract train.0.exp0 result -l train --psm 7
import os
import subprocess

def find_number_of_files(path):
    count = 153
    for base, dirs, files in os.walk(path):
        for Files in files:
            count += 1
    return int(count)


def create_text_file(path):
    for i in range(find_number_of_files(path)):
        cmd = 'tesseract train.' + str(i) + '.exp' + str(i) + '.tif ' +str(i) + ' -l train --psm 7'
        print(cmd)
        p = subprocess.Popen(cmd,cwd = path)
        p.wait()



def main():
    path = 'D:\LAGACY_TRAIN\evlution_traing_on_text'
    print(path)
    create_text_file(path)


if __name__ == "__main__":
    main()
