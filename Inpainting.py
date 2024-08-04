import numpy as np
import matplotlib.pyplot as plt
from skimage.restoration import inpaint
from skimage.transform import resize
from skimage import color

# Load your image here
defect_image = plt.imread(r"Garcia_Inpaiting.jpg")  # Ensure this path is correct
defect_image = resize(defect_image, (512, 512))

# Create a mask with the same dimensions as the image
mask = np.zeros((512, 512), dtype=bool)

# Manually define the region of the blue line (example coordinates)
# You may need to adjust these coordinates based on the actual position of the blue line
mask[30:200, 350:500] = True  # Example coordinates for the blue line

# Apply the restoration function to the image using the mask
restored_image = inpaint.inpaint_biharmonic(defect_image, mask, channel_axis=-1)

# Function to plot comparison
def plot_comparison(original, restored, title):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    ax = axes.ravel()
    ax[0].imshow(original)
    ax[0].set_title('Original Image')
    ax[1].imshow(restored)
    ax[1].set_title(title)
    for a in ax:
        a.axis('off')
    plt.tight_layout()
    plt.show()

# Show the defective and restored image
plot_comparison(defect_image, restored_image, 'Restored Image')
