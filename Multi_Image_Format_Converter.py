# -*- coding: utf-8 -*-
"""
Created on Mon May  9 14:29:21 2022

@author: KorDor
"""

from PIL import Image # required for working with images 
import os # required for working path and directory 

directory = "Datasets/obstacles_detection/train/"
outputDir = "Datasets/output/"
for filename in os.listdir(directory): 
    #if present format is png, gif or any other, then replace '.jpg' by your present format
    if filename.endswith(".jpg"):
        image=Image.open(directory + filename)
        filename_noExt, file_extension = os.path.splitext(filename)
        #replace '.tif' with required format
        image.save(outputDir + filename_noExt +'.tif','TIFF')
#%%