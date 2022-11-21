import os
import subprocess
#folder_to ='C:/Users/System Administrator/Documents/soumen_halder/Data/abc'



def create_box_file(folder_to_2):
    for i,filename in enumerate(os.listdir(folder_to_2)):
        print(filename)  
        cmd = 'tesseract -l ben --psm 7 '+ filename +' '+ filename[:-4] + ' batch.nochop makebox'
        print(cmd)   
        p = subprocess.Popen(cmd,cwd = folder_to_2)
        p.wait()


create_box_file('C:\\Users\\System Administrator\\Documents\\soumen_halder\\tt')

