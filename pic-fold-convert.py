# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 13:56:21 2020

@author: Administrator
"""



#call function imgconvertImgFormat( formatA, pathA )
# formatA : format you want, must be in '.xxx' format
# pathA : path that can be read by os. 

#e.g. imgconvertImgFormat('.png',  r'C:\Users\Administrator\Desktop\chihen')


import os
import cv2


path = r'C:\Users\Administrator\Desktop\齿痕'
imglist = []
imgnamelist = []
for img in os.listdir(path):
    imglist.append(os.path.join(path, img))
    imgnamelist.append(img)

for i in range(len(imglist)):
    os.rename(imglist[i],os.path.join(path, str(i+909 ) + '.jpg'))
    
    


def imgconvertImgFormat(formatTo, dirpath):
    imglist = []
    imgNamelist = []
    
    
    for img in os.listdir(dirpath):
        fp = os.path.join(dirpath, img)
        if os.path.isfile(fp):
            imglist.append(fp)
            imgNamelist.append(img)

    
    dirpathout = dirpath + '\Converted'
    os.mkdir(dirpathout)
    

    Tolist = []
    for img in imgNamelist:
        name, format = img.split('.')
        Tolist.append(os.path.join(dirpathout, name + formatTo))
    
    for imgs, outpath in zip(imglist,Tolist):
        img = cv2.imread(imgs)
        cv2.imwrite(outpath,img)
           
if __name__=="__main__":
    imgconvertImgFormat('.png',  r'C:\Users\Administrator\Desktop\chihen')
