import cv2
import numpy as np
import matplotlib.pyplot as plt

#IMREAD_COLOR=1 ,RGB
#IMREAD_GRAYSCALE=0
#IMREAD_UNCHANGED = -1 ,RGBA
# gray images are easier to analyse than color images due to complexity of dealing with color
img=cv2.imread("images/Picture1.jpg",cv2.IMREAD_GRAYSCALE)

#Displaying using opencv
cv2.imshow("Picture1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Displaying using matplotlib
# cmap is used pseudocolor for visualizing and enhancing contrast
#interpolation computes what the value of pixel needs to be based on mathematical calculation
plt.imshow(img,cmap="hot",interpolation='bilinear')
plt.show()

#saving onto a file
cv2.imwrite("Picture1gray.png",img)
