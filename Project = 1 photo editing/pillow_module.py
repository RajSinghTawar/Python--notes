# installation of pillowb library
# change the image extensions
# resize image files 
# resize multiple images using foe loop
# Sharpness
# Brightness
# Color
# Contrast
# Image blur, GaussianBlur


# from PIL import Image

# img1 = Image.open('rohit1.png')
# img1.save('rohit.png')
# img1.show()

# ---------- sizing ----------
# MAX_SIZE = (250,250)
# img1.thumbnail(MAX_SIZE)
# img1.save('rohitsmall.png')



# from PIL import Image
# import os

# for item in os.listdir():
#     if item.endswith('.png'):
#         img1 = Image.open(item)
#         filename,extension = os.path.splitext(item)
#         img1.save(f'{filename}.png')



# from PIL import Image, ImageEnhance
# import os
# --------- Sharpness -------------          # 0 : blurry
# img1 = Image.open('rohit.png')              # 1 : original image
# enhancer = ImageEnhance.Sharpness(img1)  # 2 : Image with increased sharpness
# enhancer.enhance(5).save('rohitedited.png')

# ---------- Color ------------
# img1 = Image.open('rohit.png')
# enhancer = ImageEnhance.Color(img1)
# enhancer.enhance(2).save('rohitedited1.png')

# ---------- Brightness -------------
# img1 = Image.open('rohit.png')
# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(1.1).save('rohitedited1.png')

# ----------- Contrast --------------
# img1 = Image.open('rohit.png')
# enhancer = ImageEnhance.Contrast(img1)
# enhancer.enhance(1.5).save('rohitedited1.png')

# from PIL import Image, ImageEnhance, ImageFilter
# import os 

# ---------- Blur ----------
# img1 = Image.open('rohit.png')
# img1.filter(ImageFilter.GaussianBlur(radius=7)).save('rohitedited.png')
