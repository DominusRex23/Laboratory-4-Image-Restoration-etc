import numpy as np
import matplotlib.pyplot as plt
from skimage.restoration import inpaint
from skimage.transform import resize
from skimage import color


defect_image = plt.imread(r"Garcia_Inpaiting.jpg")  
defect_image = resize(defect_image, (512, 512))

mask = np.zeros((512, 512), dtype=bool)

mask[30:200, 350:500] = True  

mask
restored_image = inpaint.inpaint_biharmonic(defect_image, mask, channel_axis=-1)


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


plot_comparison(defect_image, restored_image, 'Restored Image')
