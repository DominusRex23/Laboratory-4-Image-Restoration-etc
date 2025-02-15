from skimage.restoration import denoise_tv_chambolle
import matplotlib.pyplot as plt

def plot_comparison(original, modified, title):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 8), sharex=True, sharey=True)
    ax1.imshow(original)
    ax1.set_title('Original')
    ax1.axis('off')
    ax2.imshow(modified)
    ax2.set_title(title)
    ax2.axis('off')
    plt.show()


noisy_image = plt.imread(r"Garcia.jpg")  


denoised_image = denoise_tv_chambolle(noisy_image, channel_axis=-1)

plot_comparison(noisy_image, denoised_image, 'Denoised Image')
