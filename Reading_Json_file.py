# -*- coding: utf-8 -*-
"""
Created on Wed May 11 21:57:19 2022

@author: KorDor
"""
#importing the required library
import json, os


#%%
#specify the directory of the json file
directory = 'Datasets/obstacles_detection/train/'

#using for loop to go through the entire json file
for filename in os.listdir(directory):
    #using an if statement to proceed if the file is json from the directory
    if filename.endswith(".json"):
        #read the file before loading it with json library
        annotation_open = open(directory + filename,'r')
        #loading the json file using json library called loads
        annotation_load = json.loads(annotation_open.read())
        #print(annotation_load.get('imagepath'))
        #printing a specific key's contents
        print(annotation_load.get('shapes'))

#%%