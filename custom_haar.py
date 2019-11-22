# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:23:58 2019

@author: ABHI
"""
import cv2
import os
import numpy as np
import sys
import random

MAX_HARD_NEGATIVES = 20000

pos_img_dir = 'pos'
neg_img_dir = 'sampneg'

#cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)

def crop_centre(img):
    h, w, _ = img.shape
    l = (w - 64)/2
    t = (h - 128)/2

    crop = img[int(t):int(t+128), int(l):int(l+64)]
    
#    cv2.imwrite(,resized_image)
    return crop

def read_filenames():

    f_pos = []
    f_neg = []

    mypath_pos = pos_img_dir
    for (dirpath, dirnames, filenames) in os.walk(mypath_pos):
        f_pos.extend(filenames)
        break

    mypath_neg = neg_img_dir
    for (dirpath, dirnames, filenames) in os.walk(mypath_neg):
        f_neg.extend(filenames)
        break

    return f_pos, f_neg

            
def create_pos_n_neg():
    for img in os.listdir(neg_img_dir):
        line = 'pos'+'/'+img+'\n'
        with open('bg.txt','a') as f:
            f.write(line)
    for img in os.listdir(pos_img_dir):
        line = 'sempneg'+'/'+img+' 1 0 0 128 64' + '\n'
        with open('info.dat','a') as f:
            f.write(line)



pos_img_files, neg_img_files = read_filenames()

print ("Total Positive Images : " + str(len(pos_img_files)))
print ("Total Negative Images : " + str(len(neg_img_files)))
print ("Reading Images")

create_pos_n_neg()

print ("Training Started") 