import cv2

# Load your image here
img = cv2.imread('Garcia.jpg')  # Change this line

# Compress the image
cv2.imwrite('compressed_Garcia_opencv.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
