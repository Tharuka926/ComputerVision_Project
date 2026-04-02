import cv2
import numpy as np

img = cv2.imread("Resources/image02.png")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7), 0)
imgCanny = cv2.Canny(img, 150, 20)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=2)
imgEroded = cv2.erode(imgDilation, kernel, iterations=2)



cv2.imshow("Output", img)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilate Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(5000)

