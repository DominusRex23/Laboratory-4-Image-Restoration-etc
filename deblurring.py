from skimage import io, restoration
import numpy as np

# Load the image (replace 'input_image.png' with your actual image file)
input_image = io.imread('Garcia.jpg', as_gray=True)

# Apply deblurring (example using Wiener filter)
deblurred_img = restoration.wiener(input_image, psf=np.ones((5, 5)) / 25, balance=0.1)

# Convert the image to uint8
deblurred_img_uint8 = (deblurred_img * 255).astype(np.uint8)

# Save the image
io.imsave('deblurred_Garcia.jpg', deblurred_img_uint8)
