import os
import cvzone
import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(0) #video capture
detector = PoseDetector()

shirtFolderPath = "Resources/Shirts"
listShirts = os.listdir(shirtFolderPath)

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=True)  # Draw bounding box and landmarks
    
    if lmList:
        ImgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[0]), cv2.IMREAD_UNCHANGED) #for transparency of the picture 
        img = cvzone.overlayPNG(img, ImgShirt, (100, 100))

    cv2.imshow("Image", img)

    # Check for the 'q' key press to break the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord('b'):
        break

cap.release()
cv2.destroyAllWindows()
