from skimage.util import random_noise
import matplotlib.pyplot as plt


artist_image = plt.imread(r"Garcia.jpg")

noisy_image = random_noise(artist_image)


# Show the original and resulting image
def plot_comparison(original, modified, title):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 8), sharex=True, sharey=True)
    ax1.imshow(original)
    ax1.set_title('Original')
    ax1.axis('off')
    ax2.imshow(modified)
    ax2.set_title(title)
    ax2.axis('off')
    plt.show()


plot_comparison(artist_image, noisy_image, 'Noisy image')
