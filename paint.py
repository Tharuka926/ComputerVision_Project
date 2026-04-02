import cv2

# Import generic video
# cap = cv2.VideoCapture("Resources/vid01.mp4")

# Capture from webcam
cap = cv2.VideoCapture(0) # id number for webcam (0)
cap.set(3, 640) # id number for setting width of webcam (3)
cap.set(4,480) # id number for setting height of webcam (4)
cap.set(10,100) # id number for setting brightness of webcam (10)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

