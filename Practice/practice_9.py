import cv2
import numpy as np



def getContours(imag):
    contours,hierarchy = cv2.findContours(imag, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgFinal, cnt, -1, (0, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.01 * peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            ObjType = "unknown"
            if objCor == 3:
                ObjType = "triangle"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    ObjType = "square"
                else :
                    ObjType = "rectangle"
            else:
                ObjType = "circle"
            cv2.putText(imgFinal, ObjType, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

            cv2.rectangle(imgFinal, (x,y), (x+w, y+h), (0, 255, 0), 4)



img = cv2.imread("Resources/shapes.jpg")


imgFlip = cv2.flip(img, 1)
imgHor = np.vstack((imgFlip, img))
imgFinal = np.vstack((imgHor, imgHor))

imgGray = cv2.cvtColor(imgFinal, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 2)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)

cv2.imshow("Stack", imgFinal)
cv2.waitKey(0)
