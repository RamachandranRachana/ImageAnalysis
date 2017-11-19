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
    kernel = np.ones((15, 15), np.float32) / 225
    smoothed = cv2.filter2D(resblue, -1, kernel)
    blur = cv2.GaussianBlur(resblue, (15, 15), 0)
    median = cv2.medianBlur(resblue, 15)
    bilateral = cv2.bilateralFilter(resblue, 15, 75, 75)


    cv2.imshow('frame', frame)
    cv2.imshow('Averaging', smoothed)
    cv2.imshow('Gaussian Blurring', blur)
    cv2.imshow('Median Blur', median)
    cv2.imshow('bilateral Blur', bilateral)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()