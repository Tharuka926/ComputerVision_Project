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
    biggest = np.array([])
    maxArea = 0

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # Make sure detected shape is bigger than 500 pixels
        # area = 500
        if area > 500:
            # cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            # peri = perimeter
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            
            if (area > maxArea and len(approx) == 4):
                biggest = approx
                maxArea = area

    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
    
    return biggest


def reorder(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2), np.int32)

    add = myPoints.sum(1)
    # print("add", add)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]

    diff = np.diff(myPoints, axis = 1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    # print("NewPoints", myPointsNew)
    return myPointsNew
    

def getWarp(img, biggest):

    if (biggest.size == 0):
        return img
    
    biggest = reorder(biggest)
    # print(biggest)

    pts1 = np.float32(biggest)
    pts2 = np.float32([[0,0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

    return imgOutput


while True:
    success, img = cap.read()
    cv2.resize(img, (widthImg, heightImg))
    imgContour = img.copy()
    imgThreshold = preProcessing(img)

    biggest = getContours(imgThreshold)
    # print(biggest)
    imgWarped = getWarp(img, biggest)


    cv2.imshow("Result", imgWarped)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

