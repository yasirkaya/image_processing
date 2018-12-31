# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:05:40 2018

@author: Yasir
"""

import os 
from PIL import Image
from timeit import default_timer as timer

prepath = os.path.join(os.getcwd(), 'dataset-original')
glassDir = os.path.join(prepath, 'glass')
paperDir = os.path.join(prepath, 'paper')
cardboardDir = os.path.join(prepath, 'cardboard')
plasticDir = os.path.join(prepath, 'plastic')
metalDir = os.path.join(prepath, 'metal')
trashDir = os.path.join(prepath, 'trash')

destPath =os.path.join(os.getcwd(),'224-384')


''' ''' 
start = timer()
def imageResize(originalFilePath, resizeFilePath):
    try :
        os.makedirs(resizeFilePath)
    except OSError:
        if not os.path.isdir(resizeFilePath):
            raise
    for root, dirs, files in os.walk(originalFilePath) :
        for file in files:
            if len(file)<=4 or file[-4:]!='.jpg':
                continue
            pic = Image.open(os.path.join(root, file))
            genislik, yukseklik =pic.size
            if genislik >yukseklik:
                pic =pic.transpose(Image.ROTATE_270)
        
            picResized = pic.resize((224,384),Image.LANCZOS)
            picResized.save(os.path.join(resizeFilePath,file))


imageResize(glassDir, os.path.join(destPath, 'glass'))

imageResize(metalDir, os.path.join(destPath, 'metal'))

imageResize(cardboardDir, os.path.join(destPath, 'cardboard'))

imageResize(paperDir, os.path.join(destPath, 'paper'))

imageResize(plasticDir, os.path.join(destPath, 'plastic'))

imageResize(trashDir, os.path.join(destPath, 'trash'))

end = timer()

print(end-start) 


'''609.65 saniye sürdü '''



















