import numpy as np
import cv2

img = cv2.imread("images/Picture3.jpg",cv2.IMREAD_COLOR)

#Line:start,end,color,thickness
cv2.line(img,(0,0),(200,300),(255,255,255),50)

#Recangle:bottomleft,topright,color,thickness
cv2.rectangle(img,(100,250),(300,450),(0,0,255),15)

#Circle:center,radius,color,thickness (-1 to fill)
cv2.circle(img,(447,63), 63, (0,255,0), -1)

#polygon
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)

#font:text,start point,font type,size,color,thickness
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'Cat !',(100,200), font, 3, (200,255,155), 8, cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()