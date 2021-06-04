import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4, 480)
cap.set(10,100)

kernal = np.ones((5, 5), np.uint8)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgFlip = cv2.flip(img, 1)
    imgBlur = cv2.GaussianBlur(img, (17, 17), 0)
    imgCanny = cv2.Canny(img, 100, 100)
    imgDilation = cv2.dilate(imgCanny, kernal, iterations=1)
    imgErosion = cv2.erode(imgDilation, kernal, iterations=1)

    cv2.imshow("Video", imgErosion)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
