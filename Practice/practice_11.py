import numpy
import cv2

img = cv2.imread("Resources/janoooo.png")
img = cv2.resize(img, (700, 900))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 0)
imgCanny = cv2.Canny(imgBlur, 100, 100)
cv2.imshow("Output", imgCanny)
cv2.waitKey(7000)