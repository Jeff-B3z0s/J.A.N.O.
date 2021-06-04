import cv2

img = cv2.imread("Resources/gotham.jpg")


print(img.shape)
imgNew = cv2.resize(img, (450, 450))

imgCrop = img[0:900, 200:500]

cv2.imshow("Image", imgCrop)
cv2.waitKey(0)

