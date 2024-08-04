import numpy as np
from PIL import Image

def compress_image(image_path, k):
    img = Image.open(image_path)
    img_array = np.array(img) / 255.0
    
    if img_array.ndim == 3:  # Color image
        compressed_img_array = np.zeros_like(img_array)
        for i in range(3):  # Apply SVD to each channel
            U, s, V = np.linalg.svd(img_array[:, :, i], full_matrices=False)
            S = np.diag(s[:k])
            compressed_img_array[:, :, i] = np.dot(U[:, :k], np.dot(S, V[:k, :]))
    else:  # Grayscale image
        U, s, V = np.linalg.svd(img_array, full_matrices=False)
        S = np.diag(s[:k])
        compressed_img_array = np.dot(U[:, :k], np.dot(S, V[:k, :]))
    
    compressed_img = Image.fromarray((compressed_img_array * 255).astype(np.uint8))
    return compressed_img

compressed_img = compress_image('Garcia.jpg', 50)
compressed_img.save('svd_compressed_image.jpg')
