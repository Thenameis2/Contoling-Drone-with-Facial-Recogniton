import os
import cvzone
import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(0)  # video capture
detector = PoseDetector()

shirtFolderPath = "Resources/Shirts"
listShirts = os.listdir(shirtFolderPath)

# Remove the first image from the list
if listShirts:
    listShirts = listShirts[1:]
    print(listShirts)

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)

    if lmList and listShirts:
        ImgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[0]), cv2.IMREAD_UNCHANGED)  # for transparency of the picture

        # Overlay the shirt image if it's not None
        imgFront = cvzone.overlayPNG(img, ImgShirt, (100, 100))
        if imgFront is not None:
            img = imgFront

    cv2.imshow("Image", img)

    # Check for the 'q' key press to break the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord('b'):
        break

cap.release()
cv2.destroyAllWindows()
