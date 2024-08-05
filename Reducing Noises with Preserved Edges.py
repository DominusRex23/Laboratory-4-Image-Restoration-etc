from skimage.restoration import denoise_bilateral
import matplotlib.pyplot as plt


landscape_image = plt.imread(r"Garcia_noised.jpg")  
print("Image loaded:", type(landscape_image), landscape_image.shape)


denoised_image = denoise_bilateral(landscape_image, channel_axis=-1)
print("Denoising completed")


def plot_comparison(original, filtered, title):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    ax = axes.ravel()

    ax[0].imshow(original, cmap=plt.cm.gray)
    ax[0].set_title("Original Image")

    ax[1].imshow(filtered, cmap=plt.cm.gray)
    ax[1].set_title(title)

    for a in ax:
        a.axis('off')

    plt.tight_layout()
    plt.show()

plot_comparison(landscape_image, denoised_image, 'Denoised Image')
