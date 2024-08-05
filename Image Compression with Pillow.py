from PIL import Image


with Image.open('Garcia.jpg') as img:  
    
    img.save('pillow_compressed_Garcia.jpg', quality=30, optimize=True)