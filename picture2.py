import cv2
import numpy as np

img = cv2.imread("Resources/image02.png")
print(img.shape)

imgResize = cv2.resize(img, (640,480)) #Width then height
print(imgResize.shape)

imgCropped = img[0:200,100:200] #Height then width

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Crop", imgCropped)

cv2.waitKey(5000)