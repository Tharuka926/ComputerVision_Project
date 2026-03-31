import cv2

print("package imported")

img = cv2.imread("Resources/image01.png")

cv2.imshow("Output", img)

cv2.waitKey(0)