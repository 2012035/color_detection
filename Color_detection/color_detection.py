import cv2 as c
import numpy as np
# 0 34 0 255 0 255
def empty():
    pass
image=c.imread('image/wolf.jpg')
image=c.resize(image,(350,450))
c.imshow('Color_Detection',image)

c.namedWindow('Trackbar')
c.resizeWindow('Trackbar',500,270)
c.createTrackbar('Hue_Min','Trackbar',0,179,empty)
c.createTrackbar('Hue_Max','Trackbar',34,179,empty)
c.createTrackbar('Sat_Min','Trackbar',0,255,empty)
c.createTrackbar('Sat_Max','Trackbar',255,255,empty)
c.createTrackbar('Val_Min','Trackbar',0,255,empty)
c.createTrackbar('Val_Max','Trackbar',255,255,empty)


while True:
    imagehsv = c.cvtColor(image, c.COLOR_BGR2HSV)
    c.imshow('HSV',imagehsv)
    h_min=c.getTrackbarPos('Hue_Min','Trackbar')
    h_max = c.getTrackbarPos('Hue_Max', 'Trackbar')
    s_min = c.getTrackbarPos('Sat_Min', 'Trackbar')
    s_max = c.getTrackbarPos('Sat_Max', 'Trackbar')
    v_min = c.getTrackbarPos('Val_Min', 'Trackbar')
    v_max = c.getTrackbarPos('Val_Max', 'Trackbar')

    #mask is used to make change in the image using the value
    low=np.array([h_min,s_min,v_min])
    high=np.array([h_max,s_max,v_max])
    mask=c.inRange(imagehsv,low,high)
    newimage=c.bitwise_and(image,image,mask=mask)


    c.imshow('Mask_Image',mask)
    c.imshow('Detected_image',newimage)


    if(c.waitKey(1) & 0xFF == ord('z')):
        break