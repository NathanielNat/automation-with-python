from PIL import Image

im  = Image.open("beach.jpg")
    # new_img = im.resize((620,480)).rotate(90)
    # new_img.save('beach_resized_rotated.jpg')

im.resize((480,620)).save('beach_resized_saved.jpg')
# from PIL import Image
# im = Image.open("beach.jpg")
# im.rotate(45).show()