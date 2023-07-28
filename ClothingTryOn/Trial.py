import os

import cvzone
import cv2


cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()