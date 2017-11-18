import cv2
import numpy as np


img = cv2.imread("images/Picture5.jpg")

#without grayscaling
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

#after grayscaling
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('Grayscaling+ threshold',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

#adaptive thresholding
#adaptiveThreshold(src, dst, maxValue, adaptiveMethod, thresholdType, blockSize, C)
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('Grayscaling+ Adaptive threshold',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Otsu thresholding
retval,threshold = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Otsu threshold',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()