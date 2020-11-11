from PIL import Image  ## image module

import glob,os ##file path ,modules

file_size = 128,128
copy_to_path =  'opt/icons/'
# loop through all files in current folder
for infile in glob.glob('*.jpg'):
    
    file, ext =os.path.splitext(infile)
    im = Image.open(infile)
    im.resize(file_size).rotate(90).save(str(copy_to_path)+file+'.jpeg')
