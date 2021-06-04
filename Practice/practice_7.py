import cv2
import numpy as np

img = cv2.imread("Resources/gotham.jpg")

imgNew = cv2.resize(img, (450, 450))
imgHor = np.hstack((imgNew, imgNew))
imtFinal = np.vstack((imgHor, imgHor))

cv2.imshow("Stack", imtFinal)

cv2.waitKey(0)