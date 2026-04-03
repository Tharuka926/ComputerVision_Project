import cv2
import numpy as np

widthImg = 640
heightImg = 480



# Capture from webcam
cap = cv2.VideoCapture(0) # id number for webcam (0)
cap.set(3, widthImg) # id number for setting width of webcam (3)
cap.set(4,heightImg) # id number for setting height of webcam (4)
cap.set(10,130) # id number for setting brightness of webcam (10)

def preProcessing(img):
    kernel = np.ones((5,5), np.uint8)

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5), 0)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=2)
    imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

    imgThreshold = imgEroded

    return imgThreshold


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        # Make sure detected shape is bigger than 500 pixels
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            # peri = perimeter
            peri = cv2.arcLength(cnt, True)
            # print(peri)
            # approx = cv2.approxPolyDP(cnt, 0.05*peri, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h, = cv2.boundingRect(approx)



while True:
    success, img = cap.read()
    cv2.resize(img, (widthImg, heightImg))
    imgThreshold = preProcessing(img)
    cv2.imshow("Result", imgThreshold)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

