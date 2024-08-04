import cv2
import pywt
import numpy as np
from matplotlib import pyplot as plt

# Load your image here
image = cv2.imread('Garcia.jpg', 0)  

# Find the coefficients
coeffs = pywt.dwt2(image, 'bior1.3')
cA, (cH, cV, cD) = coeffs

# Plot the images
plt.subplot(121), plt.imshow(cA, cmap='gray')
plt.title('Approximation Coefficient'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cH, cmap='gray')
plt.title('Horizontal Detail Coefficient'), plt.xticks([]), plt.yticks([])
plt.show()

# Compression by applying a threshold
threshold = 20
cA_thresholded = pywt.threshold(cA, threshold, mode='soft')
cH_thresholded = pywt.threshold(cH, threshold, mode='soft')
coeffs_thresholded = (cA_thresholded, (cH_thresholded, cV, cD))
img_compressed = pywt.idwt2(coeffs_thresholded, 'bior1.3')

# Show the resulting image after compression
plt.imshow(img_compressed, cmap='gray')
plt.title('Compressed Image'), plt.xticks([]), plt.yticks([])
plt.show()
