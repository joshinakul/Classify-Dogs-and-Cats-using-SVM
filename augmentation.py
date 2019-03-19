# Importing libraries
from skimage.io import imread , imsave
from skimage.util import random_noise , invert
from skimage.transform import rotate
import os

# path of dataset
dir2 = 'dataset/'

# Counter variables
cat = 1001
dog = 1001

# Reading the complete path of all the images
imgpaths = [dir2+i for i in os.listdir(dir2)]

# Taking image one by one
for imgpath in imgpaths:
    
    if 'dog' in imgpath: # If dog is in the image name
        img = imread(imgpath) 
        noise_img = random_noise(img) # Adding noise to img
        imsave(dir2+'dog.'+str(dog)+'.jpg',noise_img) 
        dog+=1
        invert_color_img = invert(img) # Negative of img
        imsave(dir2+'dog.'+str(dog)+'.jpg',invert_color_img)
        dog+=1
        rotated_img = rotate(img,47) # Rotating img with 47 degrees
        imsave(dir2+'dog.'+str(dog)+'.jpg',rotated_img)        
        dog+=1
        horizontal_flip_img = img[:,::-1] # Fliping img horizontally
        imsave(dir2+'dog.'+str(dog)+'.jpg',horizontal_flip_img)
        dog+=1
    
    else:       # If cat is in the image name
        img = imread(imgpath)
        noise_img = random_noise(img) # Adding random noise to img
        imsave(dir2+'cat.'+str(cat)+'.jpg',noise_img)
        cat+=1
        invert_color_img = invert(img) # Negative of img
        imsave(dir2+'cat.'+str(cat)+'.jpg',invert_color_img)
        cat+=1
        rotated_img = rotate(img,47)    # Rotating img with 47 degrees
        imsave(dir2+'cat.'+str(cat)+'.jpg',rotated_img)        
        cat+=1
        horizontal_flip_img = img[:,::-1] # Fliping img horizontally 
        imsave(dir2+'cat.'+str(cat)+'.jpg',horizontal_flip_img)
        cat+=1
    
