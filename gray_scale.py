import numpy as numpy
import cv2

#Load an image in grayscale
cv2.namedWindow("Grayscale Picture", cv2.WINDOW_NORMAL)
img = cv2.imread('1_30.jpg', 0)
imgSized = cv2.resize(img, (2000,4000))
cv2.imshow("Grayscale Picture", imgSized)
cv2.waitKey(0)
cv2.destroyAllWindows()

