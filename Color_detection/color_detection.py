import cv2 as c
import numpy as np
image=c.imread('image/IMG-20220902-WA0014.jpg')
image=c.resize(image,(300,450))
c.imshow('Color_Detection',image)

while True:
    if(c.waitKey(1) & 0xFF == ord('a')):
        break