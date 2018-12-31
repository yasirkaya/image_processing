# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 14:43:05 2018

@author: Yasir
"""

import os
import imageio
import numpy as np
from os import listdir
from keras.utils import to_categorical
from scipy.misc import imread, imresize
from sklearn.model_selection import train_test_split



genislik, yukseklik = 224, 300
kanal_sayisi = 3 # 1: Grayscale, 3: RGB
etiket_sayisi = 6 # sınıf sayısı
test_verisi_orani = 0.2 # %20 test
drivePath = "drive/proje"
resimler_klasoru = os.path.join(drivePath,'224-300')
veriseti_klasoru = os.path.join(resimler_klasoru)

def resmi_al(resimler_klasoru):
    resim = imageio.imread(resimler_klasoru)
    return resim

etiketler = listdir(resimler_klasoru) 
X, Y = [], []

for i, etiket in enumerate(etiketler):
    etiket_klasoru = os.path.join(resimler_klasoru, etiket)
    
    for resim_adi in listdir(etiket_klasoru):
        resim = resmi_al(os.path.join(etiket_klasoru, resim_adi))
        X.append(resim)
        Y.append(i)
        print(resim_adi)

X = np.array(X).astype('float32')/255.
X = X.reshape(X.shape[0], genislik, yukseklik, kanal_sayisi)
Y = np.array(Y).astype('float32')
Y = to_categorical(Y, etiket_sayisi)

'''    '''   
if not os.path.exists(veriseti_klasoru):
    os.makedirs(veriseti_klasoru+'/')
 
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=test_verisi_orani, random_state=42)

np.save(os.path.join(veriseti_klasoru, 'x_train.npy'), x_train)
np.save(os.path.join(veriseti_klasoru, 'x_test.npy'), x_test)
np.save(os.path.join(veriseti_klasoru, 'y_train.npy'), y_train)
np.save(os.path.join(veriseti_klasoru, 'y_test.npy'), y_test)