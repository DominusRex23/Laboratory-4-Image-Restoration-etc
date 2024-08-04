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

# Load your image here
image_with_logo = cv2.imread(r'hito logo remove.png')

# Initialize the mask with the same shape as the image
mask = np.zeros(image_with_logo.shape[:2], dtype=np.uint8)

# Set the pixels where the logo is to 1
mask[25:200, 800:1000] = 1  # Adjust these coordinates to cover the logo accurately

# Apply inpainting to remove the logo
image_logo_removed = cv2.inpaint(image_with_logo, mask, inpaintRadius=5, flags=cv2.INPAINT_NS)

# Show the original and logo removed images
plot_comparison(image_with_logo, image_logo_removed, 'Image with logo removed')
