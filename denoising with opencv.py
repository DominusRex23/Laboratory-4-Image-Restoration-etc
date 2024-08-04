import cv2

# Load your image here
img = cv2.imread('Garcia.jpg')  # Change this line

# Apply Gaussian Blur
denoised_img = cv2.GaussianBlur(img, (5, 5), 0)

# Save the result
cv2.imwrite('denoised_Garcia.jpg', denoised_img)
