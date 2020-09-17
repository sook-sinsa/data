import numpy as np
import glob
from scipy.stats import mode
from scipy import stats
from PIL import Image

files = glob.glob('C:\\Users\\LG\\Desktop\\Hood\\*.png')
count = 0

for f in files:
    img = Image.open(f)
    rgb_img = img.convert('RGB')
    pix = np.array(img)
    
    a = pix[62][62]
    b = pix[80][80]
    c = pix[62][110]
    print(a, b, c)

    r, g, b = rgb_img.getpixel((110, 62))
    print(r, g, b)
    #print(mode(pix))
    #m = stats.mode(pix)
    #print(m)
    count = count + 1

print(count)

# pix의 형태 array([[[240, 240, 240],
    #               [240, 240, 240],
    #               [240, 240, 240],
    #                ...,
    #               [240, 240, 240],
    #               [240, 240, 240],
    #               [240, 240, 240]],

    #               [[240, 240, 240],
    #               [240, 240, 240],
    #               [240, 240, 240],

# 첫 [240, 240, 240]의 의미가 0,0 자리 pixel의 RGB값인데, 이것들을 여러개 뽑아서 최빈값으로 색을 내면 될 것 같은데 코드를 구현하지 못함...