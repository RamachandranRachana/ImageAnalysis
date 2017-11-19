import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    _, frame = cap.read()
    #In HSV the brightness value and the intensity are independent and hence easier to discriminate
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    maskred = cv2.inRange(hsv, lower_red, upper_red)
    maskblue = cv2.inRange(hsv, lower_blue, upper_blue)
    resred = cv2.bitwise_and(frame, frame, mask=maskred)
    resblue = cv2.bitwise_and(frame, frame, mask=maskblue)

    cv2.imshow('frame', frame)
    cv2.imshow('maskRed', maskred)
    cv2.imshow('maskBlue', maskblue)
    cv2.imshow('Red', resred)
    cv2.imshow('Blue', resblue)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()