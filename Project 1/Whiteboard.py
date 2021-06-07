import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,400)
cap.set(4, 400)
#cap.set(10,100)

hMin = 65
sMin = 69
vMin = 141
hMax = 179
sMax = 255
vMax = 255

#GREEN, YELLOW, RED
colors = [[49, 82, 0, 90, 255, 169], [19, 35, 171, 65, 255, 255], [116, 105, 124, 179, 255, 248]]
colorOutput = [[55, 230, 70], [0, 255, 251], [27, 24, 230]]

drawings = []

def findColor(img, color, colorOutput):

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for i in range(3):
        lower = np.array(color[i][0:3])
        upper = np.array(color[i][3:6])
        mask = cv2.inRange(imgHSV,lower,upper)

        x=0
        y=0
        w=0
        h=0
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 300:
                cv2.drawContours(img, cnt, -1, (0, 0, 255), 3)
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.01 * peri, True)
                x, y, w, h = cv2.boundingRect(approx)

        cv2.circle(img, (x + w//2, y + h //2), 10, (colorOutput[i][0], colorOutput[i][1], colorOutput[i][2]), cv2.FILLED)
        drawings.append([x + w//2, y + h//2, colorOutput[i][0], colorOutput[i][1], colorOutput[i][2]])
        #cv2.imshow(str(i), mask)



while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    findColor(img, colors, colorOutput)
    for point in drawings:
        cv2.circle(img, (point[0], point[1]), 10, (point[2],point[3],point[4]), cv2.FILLED)
    cv2.imshow("image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
