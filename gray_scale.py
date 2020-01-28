import numpy as numpy
import cv2

#Load an image in grayscale
cv2.namedWindow("Grayscale Picture", cv2.WINDOW_NORMAL)
img = cv2.imread('1_30.jpg', 0)
imgSized = cv2.resize(img, (960,540))
cv2.imshow("Grayscale Picture", imgSized)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('Gray_Scaled_1_30.jpg', img)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()

