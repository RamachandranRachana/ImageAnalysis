import numpy as np
import cv2
# view video and save video

#Loading from videosource
#cap = cv2.VideoCapture('input.avi')

#Capture from camera
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',frame)
    #cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Release Camera and file writer
cap.release()
out.release()
cv2.destroyAllWindows()