import cv2
import numpy as np


def empty(a):
    pass


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 400)
cv2.createTrackbar("hue min", "Trackbars", 0, 179, empty)
cv2.createTrackbar("hue max", "Trackbars", 179, 179, empty)
cv2.createTrackbar("sat min", "Trackbars", 31, 255, empty)
cv2.createTrackbar("sat max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("val min", "Trackbars", 92, 255, empty)
cv2.createTrackbar("val max", "Trackbars", 255, 255, empty)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4, 480)

while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hMin = cv2.getTrackbarPos("hue min", "Trackbars")
    hMax = cv2.getTrackbarPos("hue max", "Trackbars")
    sMin = cv2.getTrackbarPos("sat min", "Trackbars")
    sMax = cv2.getTrackbarPos("sat max", "Trackbars")
    vMin = cv2.getTrackbarPos("val min", "Trackbars")
    vMax = cv2.getTrackbarPos("val max", "Trackbars")
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])
    mask = cv2.inRange(imgHSV,lower,upper)

    finalImg = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("MASK", finalImg)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break