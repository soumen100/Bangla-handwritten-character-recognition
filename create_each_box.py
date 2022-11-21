import os
import numpy as np
from PIL import Image as im

#os.chdir(r"D:\LSTM TRAIN\out_put\1")


my_rec = 50
sp = 10
text_file_path = 'D:\\LAGACY_TRAIN\\bagaliy_word_list.txt'


word_list = []

def get_charter_in_list():
    with open(text_file_path,mode = 'r', encoding="utf-8") as f:
        for i,line in enumerate(f):
            for i,character in enumerate(line):
                if(character == ' '):
                    word_list.append('sss')
                elif(character == '\n'):
                    word_list.append('bbb')
                else:
                    word_list.append(character)
    return word_list

sp = 10
rec = 100  
hight = 150

def write_box_file(p, word_list):  
    count = 0
    cord = 0
    prev_y = 0
    current_y = 50
    t = 'train.' + str(count) +'.exp'+str(count) + '.box'
    t = os.path.join(p, t)
    f = open(t, "a", encoding="utf-8")
    for ch in word_list:
        if ch == 'sss':
            #print(cord)
            #s = ' ' + ' '+str(cord) + ' ' + str(rec)+' '+str(sp) +' '+str(sp) + ' ' + str(0) + '\n'
            #f.write(s)
            cord = cord + 10
            
            #continue
            #print(cord)
            
        elif ch != 'bbb':
            #print(cord)
            current_y = 50+ cord
            s = ch + ' '+str(cord) + ' ' + str(rec)+' '+str(current_y)+' '+str(hight) + ' ' + str(0)+ '\n'
            f.write(s)
            cord = cord + 50
            #print(cord)
            
        else:
            f.close()
            cord = 0
            prev_y = 0
            count = count + 1            
            t =  'train.' + str(count) +'.exp'+str(count) + '.box'
            t = os.path.join(p, t)
            f = open(t, "a", encoding="utf-8")

def main():
    save_path = "D:\\LAGACY_TRAIN\\marge_2"
    word_list = get_charter_in_list()
    write_box_file(save_path,word_list)
    
    
    
if __name__ == "__main__":
    main()