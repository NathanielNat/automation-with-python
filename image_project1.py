from PIL import Image  ## image module

import glob,os ##file path ,modules

file_size = 640,640
# loop through all files in current folder
for infile in glob.glob('*.jpg'):
    theta = 90
    file, ext =os.path.splitext(infile)
    im = Image.open(infile)
    im.resize(file_size).rotate(angle = theta).save(file+'.jpg')
