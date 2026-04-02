import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
print(img)

# img[:] = 255,0,0 #Blue full image
# img[200:300,100:300] = 255,0,0 #200:300 is height, 100:300 is width
# cv2.line(img,(0,0),(300,300),(0,255,0),3) #(0,0) is starting point, (300,300) is ending point, (0,255) is colour, 3 is width
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) # img.shape[1] is width, img.shape[0] is height

cv2.rectangle(img,(0,0),(250,350),(0,0,255), cv2.FILLED)
cv2.circle(img,(400,50),30,(255,255,0),5)

cv2.imshow("Image", img)


cv2.waitKey(0)