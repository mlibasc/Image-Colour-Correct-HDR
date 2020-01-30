import numpy as numpy
import cv2

width = 500
height = 500
buff = 0.0
gamma = 1.0

#Load an image in grayscale
cv2.namedWindow("Grayscale Picture", cv2.WINDOW_NORMAL)
img_30_shutter = cv2.imread('1_30.jpg', 0)
img_60_shutter = cv2.imread('1_60.jpg', 0)
corrected = cv2.imread('1_60.jpg', 0)

img_30_shutter = cv2.resize(img_30_shutter, (width,height))
img_60_shutter = cv2.resize(img_60_shutter, (width,height))
corrected = cv2.resize(corrected, (width,height))

for i in range(width):
    for j in range(height):
        buff = ((img_60_shutter[i][j] ** (1/gamma)) * 2) ** gamma
        if(buff > 255):
            corrected[i][j] = 255
        else:
            corrected[i][j] = buff
        
        
cv2.destroyAllWindows()
cv2.imshow("Grayscale Picture 30 Shutter Speed", img_30_shutter)
cv2.imshow("Grayscale Picture 60 Shutter Speed", img_60_shutter)
cv2.imshow("Grayscale Picture Corrected", corrected)

k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('Grayscale_Corrected_60SS.jpg', corrected)
    cv2.imwrite('Grayscale_30SS.jpg', img_30_shutter)
    cv2.imwrite('Grayscale_60SS.jpg', img_60_shutter)
    print("Image written to file-system: ", status)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()