# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:16:38 2019

@author: Naurin
"""

import numpy as np
import cv2


#this is the cascade we just made. Call what you want
watch_cascade = cv2.CascadeClassifier('data\stage19.xml')
orig = cv2.imread('sample_images\crop_000001.png')
img = orig.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

watches = watch_cascade.detectMultiScale(gray, 20, 20)

# add this
for (x,y,w,h) in watches:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)


roi_gray = gray[y:y+h, x:x+w]
roi_color = img[y:y+h, x:x+w]

cv2.imshow('img',img)
k = cv2.waitKey(30)
cv2.destroyAllWindows()