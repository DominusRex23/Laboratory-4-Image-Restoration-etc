import cv2

img = cv2.imread('Garcia.jpg')  

denoised_img = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imwrite('denoised_Garcia.jpg', denoised_img)
