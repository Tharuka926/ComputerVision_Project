import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width,height = 250,350

pts1 = np.float32([[117,44], [232,72], [32,124], [166,162]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Warp", imgOutput)

cv2.waitKey(5000)
