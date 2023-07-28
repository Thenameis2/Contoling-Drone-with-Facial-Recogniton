import os
import cv2
import numpy as np
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(0)  # video capture
detector = PoseDetector()

shirtFolderPath = "Resources/MyShirts"
listShirts = os.listdir(shirtFolderPath)

# Remove the first image from the list
if listShirts:
    listShirts = listShirts[1:]
    print(listShirts)

# Load the first shirt image
if listShirts:
    ImgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[0]), cv2.IMREAD_UNCHANGED)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (640, 480))  # Resize for consistency
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)

    if lmList and listShirts:
        # Get the coordinates of the relevant landmarks from lmList
        lm11 = lmList[11][1:3]  # left shoulder landmark
        lm12 = lmList[12][1:3]  # right shoulder landmark

        # Calculate the width of the shirt based on the distance between shoulders
        widthOfShirt = int(np.linalg.norm(np.array(lm11) - np.array(lm12)) * 2)  # Adjust the scaling factor (1.5) as needed

        # Calculate the height of the shirt based on the aspect ratio of the shirt image
        shirtAspectRatio = ImgShirt.shape[1] / ImgShirt.shape[0]
        heightOfShirt = int(widthOfShirt / shirtAspectRatio)

        # Create points for perspective transformation and adjust the position
        offset_x = 0  # Adjust the horizontal position offset
        offset_y = 80  # Adjust the vertical position offset
        pts1 = np.float32([[0, 0], [ImgShirt.shape[1], 0], [ImgShirt.shape[1], ImgShirt.shape[0]], [0, ImgShirt.shape[0]]])
        pts2 = np.float32([[lm11[0] - widthOfShirt // 2 - offset_x, lm11[1] - offset_y],
                           [lm12[0] + widthOfShirt // 2 + offset_x, lm11[1] - offset_y],
                           [lm12[0] + widthOfShirt // 2 + offset_x, lm11[1] + heightOfShirt + offset_y],
                           [lm11[0] - widthOfShirt // 2 - offset_x, lm11[1] + heightOfShirt + offset_y]])

        # Perform perspective transformation
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgWarp = cv2.warpPerspective(ImgShirt, matrix, (img.shape[1], img.shape[0]))

        # Overlay the shirt image with alpha blending
        for c in range(0, 3):
            img[:, :, c] = img[:, :, c] * (1 - imgWarp[:, :, 3] / 255.0) + imgWarp[:, :, c] * (imgWarp[:, :, 3] / 255.0)

    cv2.imshow("Image", img)

    # Check for the 'q' key press to break the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord('b'):
        break

cap.release()
cv2.destroyAllWindows()
