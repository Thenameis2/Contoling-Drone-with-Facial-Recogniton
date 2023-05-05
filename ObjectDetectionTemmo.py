import cv2
import numpy as np

global imgContour
global dir
def empty(a):
    pass
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("HUE Min", "HSV", 20, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 40, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 148, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("Value Min", "HSV", 89, 255, empty)
cv2.createTrackbar("Value Max", "HSV", 255, 255, empty)

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 166, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 171, 255, empty)
cv2.createTrackbar("Area", "Parameters", 1750, 30000, empty)

def stackImage(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvaialiable =isinstance(imgArray[0],list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvaialiable:
        for x in range(0,rows):
            for y in range(0,cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y],(0,0), None,scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y],(imgArray[0][0].shape[1],imgArray[0][0].shape[0]), None,scale, scale)
                if len(imgArray[x][y].shape) == 2:imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageblank = np.zeros((height,width,3),np.uint8)
        hor = [imageblank]*rows
        hor_con = [imageblank]*rows
        for x in range(0,rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0,rows):
             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                 imgArray[x] = cv2.resize(imgArray[x],(0,0), None,scale, scale)
             else:
                imgArray[x] = cv2.resize(imgArray[x],(imgArray[0].shape[1],imgArray[0].shape[0]), None,scale, scale)
             if len(imgArray[x].shape) == 2:imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor =np.hstack(imgArray)
        ver = hor
        return ver
stackImage(scale,imgArray)



                

    
