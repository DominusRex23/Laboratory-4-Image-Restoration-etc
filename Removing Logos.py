import numpy as np
import cv2
import matplotlib.pyplot as plt

def plot_comparison(original, modified, title):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    ax = axes.ravel()
    ax[0].imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    ax[0].set_title('Original Image')
    ax[1].imshow(cv2.cvtColor(modified, cv2.COLOR_BGR2RGB))
    ax[1].set_title(title)
    for a in ax:
        a.axis('off')
    plt.tight_layout()
    plt.show()

image_with_logo = cv2.imread(r'hito logo remove.png')

mask = np.zeros(image_with_logo.shape[:2], dtype=np.uint8)

mask[25:200, 800:1000] = 1  

image_logo_removed = cv2.inpaint(image_with_logo, mask, inpaintRadius=5, flags=cv2.INPAINT_NS)

plot_comparison(image_with_logo, image_logo_removed, 'Image with logo removed')
