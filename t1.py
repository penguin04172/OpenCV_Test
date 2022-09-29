import cv2
import numpy as np

cap = cv2.VideoCapture('v1.mp4')

while (True) :
    ret, frame = cap.read()

    if not ret :
        break

    # frame = np.uint8(np.clip((1.5 * frame + 10), 0, 255))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 100, 230])
    upper = np.array([20, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7,7), 0)
    ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)

    dil = cv2.dilate(thresh, np.ones((13,13), np.uint8))
    ero = cv2.erode(dil, np.ones((5,5), np.uint8))

    cnts = cv2.findContours(ero, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts[0]:
        if cv2.contourArea(c) > 200:
            (x,y,w,h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    cv2.imshow('frame', frame)

    if (cv2.waitKey(1) & 0xff == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
