import cv2

img = cv2.imread('Garcia.jpg')  

cv2.imwrite('compressed_Garcia_opencv.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
