import os
import glob
from PIL import Image

files = glob.glob('C:\\Users\\LG\\Desktop\\Hood\\*.png')

for f in files:
    img = Image.open(f)
    img_resize = img.resize((125, 125), Image.ANTIALIAS)
    title, ext = os.path.splitext(f)
    img_resize.save(title + '_change' + ext)

# 배경을 덧붙이지 않고, 그림 자체를 늘리고 줄이고 해서 (125,125) size로 맞춰줌