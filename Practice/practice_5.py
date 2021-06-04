import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
#img[200:300, 100:300] = 255, 0, 0
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (250, 10, 255))

cv2.rectangle(img, (50,50), (75, 100), (250, 250, 0), cv2.FILLED)
cv2.circle(img, (300,300), 50, (40, 255, 150), cv2.FILLED)
cv2.putText(img, "OPENCV TEXT GANG", (50,150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)


cv2.imshow("Image", img)
cv2.waitKey(0)

