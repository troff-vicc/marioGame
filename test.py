from PIL import Image
im = Image.open('Mario/tecsture/NES - Super Mario Bros - Mario & Luigi.png')
im_crop = im.crop((0, 8, 16, 24))
#im_crop.show()
im_crop.save('Mario/tecsture/mario.png')