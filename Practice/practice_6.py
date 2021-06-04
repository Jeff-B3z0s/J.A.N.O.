import cv2
import numpy as np

#Random Warping
img = cv2.imread("Resources/gotham2.jpg")

width = img.shape[0]
height = img.shape[1]

pts = np.float32([[11,89], [22, 99], [16, 150], [86, 200]])
pts2 = np.float32([[0,0],[width,0], [0,height], [width,height]])
matrix = cv2.getPerspectiveTransform(pts, pts2)

imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Image", imgOutput)
cv2.waitKey(0)