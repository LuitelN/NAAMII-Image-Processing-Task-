import cv2 as cv 
import numpy as np 

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#img = cv.imread('Cat.png')
#cv.imshow('Cat', img)
#blank[:] = 0,255,255 #Yellow
#blank[:] = 0,255,0 #Green 
blank[:] = 0,0,255 #Red 

cv.imshow('Green', blank)
cv.waitKey(0)