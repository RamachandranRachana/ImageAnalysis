import cv2
import numpy

img=cv2.imread("images/Picture4.jpg",1)
img = cv2.resize(img, (960, 540))
#img[50:350,450:820] = [255,255,255]
tiger_face = img[50:350,450:820]
img[0:300,0:370] = tiger_face
cv2.imshow("Picture1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()