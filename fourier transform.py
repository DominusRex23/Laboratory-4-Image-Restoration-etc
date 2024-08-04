import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load your image here
image = cv2.imread('Garcia.jpg', 0)  # Change this line

# Apply the Fourier transform
f_transform = np.fft.fft2(image)
f_transform_shifted = np.fft.fftshift(f_transform)
magnitude_spectrum = np.log(np.abs(f_transform_shifted) + 1)

# Plot the images for comparison
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

# Compression by discarding high-frequency components
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2
f_transform_shifted[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0
f_transform_inverse = np.fft.ifftshift(f_transform_shifted)
img_back = np.fft.ifft2(f_transform_inverse)
img_back = np.abs(img_back)

plt.imshow(img_back, cmap='gray')
plt.title('Compressed Image'), plt.xticks([]), plt.yticks([])
plt.show()
