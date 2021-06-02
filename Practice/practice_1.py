import numpy
import cv2
print('functioning')

img = cv2.imread("Resources/colors.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Output", imgGray)
cv2.waitKey(7000)
