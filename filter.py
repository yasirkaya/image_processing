#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 13:40:42 2018

@author: yasir
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


mask_1=np.random.randint(5,size=9).reshape(3,3)
mask_2=np.random.randint(5,size=9).reshape(3,3)



def get_default_mask_for_mean():
    return np.array([1, 1, 1, 1, 1, 1, 1, 1, 1]).reshape(3, 3)/9
def apply_mask(part_of_image):
    mask=get_default_mask_for_mean()
    return sum(sum(part_of_image*mask))


image_1=plt.imread("indir.jpeg");

def get_median(poi):
    s_1=poi.reshape(1,9)
    s_1.sort()
    return s_1[0,4]/3

def get_distance(v,w=[1/3,1/3,1/3]): 
    a,b,c = v[0],v[1],v[2]
    w1,w2,w3 = w[0],w[1],w[2]
    d = ((a**2)*w1+
    (b**2)*w2+
    (c**2)*w3)**.5
    return d

def convert_rgb_to_gray_level(im_1):
    m=im_1.shape[0]
    n=im_1.shape[1]
    im_2 = np.zeros((m,n)) 
    for i in range(m):
        for j in range(n):
            im_2[i,j] = get_distance(im_1[i,j,:])
    return im_2
def get_mean_filter(image_1):
    m = image_1.shape[0]
    n = image_1.shape[1]
    image_2=np.zeros((m,n))
    
    for i in range (1,m-1):
        for j in range(1,n-1):
            poi=image_1[i-1:i+2,j-1:j+2]
            
            image_2[i,j]=get_median(poi)
    return image_2

imageGray=convert_rgb_to_gray_level(image_1)
median=get_mean_filter(imageGray)
plt.subplot(1,2,1)
plt.imshow(median,cmap="gray")
plt.subplot(1,2,2)
plt.imshow(imageGray,cmap="gray")
plt.show()