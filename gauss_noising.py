import numpy as np
import os
import cv2
import matplotlib.image as mp
import matplotlib.pyplot as plt
##def noisy(image):
##      row=len(image)
##      col= len(image[0])
##      mean = 0
##      var = 0.1
##      sigma = var**0.5
##      gauss = np.random.normal(mean,sigma,(row,col))
##      gauss = gauss.reshape(row,col)
##      noisy = image + gauss
##      return noisy
image=cv2.imread('pic_10.jpg',0)
row=len(image)
col=len(image[0])
mean=0
var=0.1
sigma=var**0.5
gauss = np.random.normal(mean,sigma,(row,col))
gauss=gauss.reshape(row,col)
noisy=image+gauss
cv2.imwrite('gaussian_pic10.png',noisy)
cmap=plt.get_cmap('gray')
plt.imshow(noisy,cmap)
##img1=cv2.imread('gaussian_pic10.png',0)
##plt.hist(img1.ravel(),256,[0,256])
plt.show()
