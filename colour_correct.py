import cv2
import numpy as np
import matplotlib.pyplot as plt 

#red gamma =  0.9820000000000001
#green gamma = 0.9820000000000001
#blue gamma =  0.9820000000000001
#red error =  1212.8656978087354
#green error =  1891.6883198776327
#blue error =  3361.3955247984823

#variable declaration
width = 500
height = 500

iterations = 50
min_gamma_red = 0.1
min_gamma_green = 0.1
min_gamma_blue = 0.1
max_gamma_red = 1
max_gamma_green = 1
max_gamma_blue = 1

increment_r = (max_gamma_red-min_gamma_red)/iterations
increment_g = (max_gamma_green-min_gamma_green)/iterations
increment_b = (max_gamma_blue-min_gamma_blue)/iterations

gamma_r = [None]*iterations
gamma_g = [None]*iterations
gamma_b = [None]*iterations

errors_r = [None]*iterations
errors_g = [None]*iterations
errors_b = [None]*iterations

err_r = [None]*iterations
err_g = [None]*iterations
err_b = [None]*iterations

best_err_r = 100
best_err_g = 100
best_err_b = 100
best_gam_r = 0
best_gam_g = 0
best_gam_b = 0

def MeanSquaredError(target, corrected, idx):
    mse = 0
    for i in range(width):
        for j in range(height):
            mse += ((target[i][j][idx]/255 - corrected[i][j][idx]/255) ** 2)
    return mse 

def Correction(target, ref, gamma, idx):
    inv_gamma = 1/gamma
    for i in range(width):
        for j in range(height):
            temp = (ref[i][j][idx] ** (inv_gamma) * 2) ** gamma
            if(temp > 255):
                target[i][j][idx] = 255
            else:
                target[i][j][idx] = temp
    return target

def BestNum(error, currentError, gam, idx):
    best_gam = 0
    if(error < currentError):
        currentError = error
        best_gam = gam[idx] 
    return currentError, best_gam;

#loading images with colour
cv2.namedWindow("Colour Correction", cv2.WINDOW_NORMAL)
img30 = cv2.imread('1_30.jpg')
img60 = cv2.imread('1_60.jpg')
corrected = cv2.imread('1_60.jpg')

img30 = cv2.resize(img30, (width, height))
img60 = cv2.resize(img60, (width, height))
corrected = cv2.resize(corrected, (width, height))

#incrementing from min_gamma to max_gamma with iterations
for i in range(iterations):
    gamma_r[i] = min_gamma_red + i*increment_r
    gamma_g[i] = min_gamma_green + i*increment_g
    gamma_b[i] = min_gamma_blue + i*increment_b

#correcting image
for i in range(iterations):
    print("red gamma = ", gamma_r[i])
    print("green gamma = ", gamma_g[i])
    print("blue gamma = ", gamma_b[i])
    corrected = Correction(corrected, img60, gamma_r[i], 0)
    corrected = Correction(corrected, img60, gamma_g[i], 1)
    corrected = Correction(corrected, img60, gamma_b[i], 2)

    err_r[i] = MeanSquaredError(corrected, img30, 0)
    err_g[i] = MeanSquaredError(corrected, img30, 1)
    err_b[i] = MeanSquaredError(corrected, img30, 2)
    print("red error = ", err_r[i])
    print("green error = ", err_g[i])
    print("blue error = ", err_b[i])
    
    best_err_r, best_gam_r = BestNum(err_r[i], best_err_r, gamma_r, i)
    best_err_g, best_gam_g = BestNum(err_g[i], best_err_g, gamma_g, i)
    best_err_b, best_gam_b = BestNum(err_b[i], best_err_b, gamma_b, i)

plt.plot(gamma_r, err_r, 'r',gamma_g, err_g, 'g', gamma_b, err_b, 'b')
plt.suptitle('error for each gamma')
plt.xlabel('gamma')
plt.ylabel('mean squared error')
plt.show()

cv2.destroyAllWindows()
cv2.imshow("Image with 1/30 shutter speed", img30)
cv2.imshow("Image with 1/60 shutter speed", img60)
cv2.imshow("Corrected image", corrected)

k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite('Corrected_60SS.jpg', corrected)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()
