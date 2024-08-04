from PIL import Image

# Open an image file
with Image.open('Garcia.jpg') as img:  # Change this line
    # Compress the image
    img.save('pillow_compressed_Garcia.jpg', quality=30, optimize=True)