import cv2
import numpy as np

# Capture from webcam
cap = cv2.VideoCapture(0) # id number for webcam (0)
cap.set(3, 640) # id number for setting width of webcam (3)
cap.set(4,480) # id number for setting height of webcam (4)
cap.set(10,110) # id number for setting brightness of webcam (10)



# pink, blue, green
myColours = [[139, 21, 72, 179, 253, 179], [102, 70, 110, 126, 239, 179], [49, 41, 82, 79, 255, 255]]
colorNames = ["Pink", "Blue", "Green"]
myColourValues = [[188, 99, 255], [255, 119,0], [57, 138, 0]]
colourCycleCount = 0

myPoints = [] #[x, y, colourID]

def findColor(img, myColours, colourCycleCount, myColourValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColours:
        lower =  np.array(color[0:3]) 
        upper =  np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgFinal, (x,y), 10, myColourValues[count], cv2.FILLED)
        # cv2.imshow("Img", mask)
        # imgResult = cv2.bitwise_and(img, img, mask=mask)
        # cv2.imshow(str(colorNames[counter]), imgResult)
        if (x != 0 and y != 0):
            newPoints.append([x,y,count])
        colourCycleCount += 1
        count += 1

    return newPoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,w,y,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # Make sure detected shape is bigger than 500 pixels
        if area > 500:
            # cv2.drawContours(imgFinal, cnt, -1, (255, 0, 0), 3)
            # peri = perimeter
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h, = cv2.boundingRect(approx)
    return x+w//2, y


def drawOnCanvas(myPoints, myColourValues):
    for point in myPoints:
        cv2.circle(imgFinal, (point[0], point[1]), 10, myColourValues[point[2]], cv2.FILLED)



while True:
    success, img = cap.read()
    imgFinal = img.copy() 
    newPoints = findColor(img, myColours, colourCycleCount, myColourValues)

    if (newPoints != 0):
        for newP in newPoints:
            myPoints.append(newP)

    if (len(myPoints) != 0):
        drawOnCanvas(myPoints, myColourValues)

    cv2.imshow("Video", imgFinal)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    


    cv2.waitKey(1)
