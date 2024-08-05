from skimage import io, restoration
import numpy as np

input_image = io.imread('Garcia.jpg', as_gray=True)

deblurred_img = restoration.wiener(input_image, psf=np.ones((5, 5)) / 25, balance=0.1)


deblurred_img_uint8 = (deblurred_img * 255).astype(np.uint8)

io.imsave('deblurred_Garcia.jpg', deblurred_img_uint8)
