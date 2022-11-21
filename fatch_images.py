import pandas as pd
import os
import random
import re
from PIL import Image  
import PIL 
import cv2
  #return res

#def save_file(random_filename):
import bangla
#bangla_numeric_string = bangla.convert_english_digit_to_bangla_digit("123456") 
def normalize(x,i):       
    img = cv2.imread(x, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (50,50),interpolation = cv2.INTER_NEAREST)
    img = Image.fromarray(img)
    return img
    #print(img)
    #s = str(i) + '.jpg'
    #img.save(s)

def open_file(new_path):
    print(new_path)
    #os.chdir(p)
    #print(os.getcwd())
    random_filename = random.choice([
        x for x in os.listdir(new_path)
        if os.path.isfile(os.path.join(new_path, x))
        ])
    #print(random_filename)
    #save_file(random_filename)
    img = cv2.imread(os.path.join(new_path, random_filename), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (50,50),interpolation = cv2.INTER_NEAREST)
    r = Image.fromarray(img)    
    return(r, random_filename)

def location(df,character,retival_path):
     for i in range(len(df.Label)):
         print(character, bangla.convert_english_digit_to_bangla_digit( df.Char_Name[i]))
         if(character == bangla.convert_english_digit_to_bangla_digit( df.Char_Name[i])):
             indx = i
             break
     #print(df.Label[indx])    
     s = df.Label[indx]
     retival_path = 'C:\\Users\\System Administrator\\Documents\\soumen_halder\\working\\raw\\male'
     new_path = retival_path +'\\'+ str(s)
     print(new_path)
     return(open_file(new_path))

def take_Get_location(csvfile,retival_path):
    abcpath = 'D:\\LAGACY_TRAIN\\double_train'

    with open("D:\\LAGACY_TRAIN\\bagaliy_word_list.txt",mode = 'r', encoding="utf-8") as f:
        for i,line in enumerate(f):
            new_folder = os.path.join(abcpath, str(i)) 
            print(new_folder)
            os.mkdir(str(new_folder))
            count = 0
            print(retival_path)
            for i,character in enumerate(line):
               #
                if(character == ' ' or character == '\n'):
                    continue 
                else:
                    #print(character)
                    print(retival_path)
                    r,m = location(csvfile,character,retival_path)
                    #picture = Image.open(r)  
                    #picture.show()
                    #r = normalize(r,i)
                    p = new_folder + '\\' + str(count) + '.jpg'
                    count = count +1
                    r.save(p)
                    #pass


def main():
    #os.chdir("D:\LAGACY_TRAIN\numerical_out")
    csvfile = pd.read_excel("C:\\Users\\System Administrator\\Documents\\soumen_halder\\working\\raw\\Book1.xlsx", )
    #print(csvfile.head())
    #print(csfile['Char_Name'])
    path = "D:\\LAGACY_TRAIN\\raw_numerical_data"
    print(path)
    take_Get_location(csvfile,path)
    
if __name__ == "__main__":
    main()