import os
import numpy as np
from PIL import Image as im

#os.chdir(r"D:\LSTM TRAIN\out_put\1")

def create_background_image():
    img_1 = np.zeros([200,1000],dtype=np.uint8)
    img_1.fill(255)
    data = im.fromarray(img_1)
    return data


def paste_iamges(data_path,save_path,m):
    space = 0 
    n_p = ''
    img = create_background_image()
    num = 0
    #print(p)
    for i,x in enumerate(os.listdir(data_path)):
            t = str(num) + '.jpg'
            x = os.path.join(data_path, t )
            print(x)
            img2 = im.open(x) 
            img.paste(img2, (space, 50))
            space = space + 50 + 10
            num = num + 1  
    n_p = save_path  +'\\'+'train.' + m +'.exp'+m+ '.tif'
    img.save(n_p)

    
    
def main():
    #data_path = "D:\\LSTM TRAIN\\out_put\\1"
    for i,x in enumerate(os.listdir('D:\\LAGACY_TRAIN\\double_train' )):
        print(i,x)
        data_path =  'D:\\LAGACY_TRAIN\\double_train\\' + str(i)
        print(data_path)
        save_path = "D:\LAGACY_TRAIN\marge_2"
        print(str(x))
        paste_iamges(data_path, save_path, str(i))
    
if __name__ == "__main__":
    main()