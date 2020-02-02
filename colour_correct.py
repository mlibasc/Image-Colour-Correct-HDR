import cv2
import numpy as np 

width = 500
height = 500
gamma = 0.73
buffRed = 0.0
buffGreen = 0.0
buffBlue = 0.0
mseRed = 0.0
mseGreen = 0.0
mseBlue = 0.0

#Loading images with colour
cv2.namedWindow("Colour Correction", cv2.WINDOW_NORMAL)
img30 = cv2.imread('1_30.jpg')
img60 = cv2.imread('1_60.jpg')
corrected = cv2.imread('1_60.jpg')

img30 = cv2.resize(img30, (width, height))
img60 = cv2.resize(img60, (width, height))
corrected = cv2.resize(corrected, (width, height))

for i in range(width):
    for j in range(height):
        buffRed = (img60[i][j][0] ** (1/gamma) * 2) ** gamma
        buffGreen = (img60[i][j][1] ** (1/gamma) * 2) ** gamma
        buffBlue = (img60[i][j][2] ** (1/gamma) * 2) ** gamma
        if(buffRed > 255):
            corrected[i][j][0] = 255
        else:
            corrected[i][j][0] = buffRed
        if(buffGreen > 255):
            corrected[i][j][1] = 255
        else: 
            corrected[i][j][1] = buffGreen
        if(buffBlue > 255):
            corrected[i][j][2] = 255
        else: 
            corrected[i][j][2] = buffBlue
        mseRed += ((img30[i][j][0]/255 - corrected[i][j][0]/255) ** 2)
        mseGreen += ((img30[i][j][1]/255 - corrected[i][j][1]/255) ** 2)
        mseBlue += ((img30[i][j][2]/255 - corrected[i][j][2]/255) ** 2)

mseRed = mseRed #/ (width * height)
mseGreen = mseGreen #/ (width * height)
mseBlue = mseBlue #/ (width * height)

cv2.destroyAllWindows()
cv2.imshow("Image with 1/30 shutter speed", img30)
cv2.imshow("Image with 1/60 shutter speed", img60)
cv2.imshow("Corrected image", corrected)

print ("gamma = ", gamma)
print ("mseRed = ", mseRed)
print ("mseGreen = ", mseGreen)
print ("mseBlue = ", mseBlue)

k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('Corrected_60SS.jpg', corrected)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()