#tesseract train.my.exp0.tif train.my.exp0 box.train
#unicharset_extractor train.my.exp0.box
# mftraining -F font_properties -U unicharset -O train.unicharset train.my.exp0.tr
#cntraining train.my.exp0.tr
import os
import subprocess

def find_number_of_files(path):
    count = 0
    for base, dirs, files in os.walk(path):
        for Files in files:
            count += 1
    #return int(count/2)
    return int(1485)

def create_laggacy__dot_train_file(path):
    l = find_number_of_files(path)
    #l = 6
    for i in range(l):
        cmd = 'tesseract train.' + str(i) + '.exp'+str(i)+'.tif '+ 'train.'+ str(i) + '.exp'+str(i) + ' box.train'
        print(cmd)
        p = subprocess.Popen(cmd,cwd = path)
        p.wait()
       
def create_uni_cracter(path):
    list_name = '' 
    l = find_number_of_files(path)
    for i in range(l):
        cmd = 'train.' + str(i) + '.exp'+ str(i) + '.box '
        list_name = list_name + cmd
    print(list_name)
    cmd = 'unicharset_extractor ' + list_name
    p = subprocess.Popen(cmd,cwd = path)
    p.wait()
    
def get_names(path):
    list_name = '' 
    l = find_number_of_files(path)
    for i in range(l):
        cmd = 'train.' + str(i) + '.exp'+ str(i) + '.tr '
        list_name = list_name + cmd
    return list_name

def create_mftraining(path):
    list_name = get_names(path)
    cmd = 'mftraining -F font_properties -U unicharset -O train.unicharset ' + list_name
    print(cmd)
    p = subprocess.Popen(cmd,cwd = path)
    p.wait()

def cntraining(path):
    list_name = get_names(path)
    cmd = 'cntraining '+ list_name
    print(cmd)
    p = subprocess.Popen(cmd,cwd = path)
    p.wait()

def main():
    path = "D:\LAGACY_TRAIN\marge_2"
    ##create_laggacy__dot_train_file(path)
    #create_uni_cracter(path)
    #create_mftraining(path)
    cntraining(path)
    

if __name__ == "__main__":
    main()