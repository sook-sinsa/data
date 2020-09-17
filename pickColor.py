import os
from PIL import Image
import openpyxl
import numpy
import math

try:
    wb = openpyxl.load_workbook("collected/datasheet2.xlsx")
    sheet = wb.active
    print("불러오기 완료")

except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["대 카테고리", "세부 카테고리", "제품 번호", "R", "G", "B"])
    print("새로 파일을 만들었습니다")

itemCategory = [
    [0,1,2,3,4,5,6,7,8],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
    [0,1,2,3],
    [0,1,2,3,4,5,6],
    [0,1,2]
]

for x in range(len(itemCategory)):
    bigCategory = x
    for y in range(len(itemCategory[x])):
        smallCategory = y
        
        img_dir = './collected/image/'+str(bigCategory)+'/'+str(smallCategory)
        
        for i in range(len(os.listdir(img_dir))-1):
            img_path = os.path.join(img_dir,str(i)+'.png')
            img = Image.open(img_path)
            rgb_img = img.convert('RGB')

            r1, g1, b1 = rgb_img.getpixel((62,62))
            r2, g2, b2 = rgb_img.getpixel((62,63))
            r3, g3, b3 = rgb_img.getpixel((63,62))
            r4, g4, b4 = rgb_img.getpixel((63,63))
            r5, g5, b5 = rgb_img.getpixel((61,62))
            r6, g6, b6 = rgb_img.getpixel((61,63))
            r7, g7, b7 = rgb_img.getpixel((64,62))
            r8, g8, b8 = rgb_img.getpixel((64,63))
            r9, g9, b9 = rgb_img.getpixel((61,62))
            r10, g10, b10 = rgb_img.getpixel((61,63))
            r11, g11, b11 = rgb_img.getpixel((64,62))
            r12, g12, b12 = rgb_img.getpixel((64,63))

            r = math.floor(numpy.mean([r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12]))
            g = math.floor(numpy.mean([g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12]))
            b = math.floor(numpy.mean([b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12]))

            sheet.append([bigCategory, smallCategory, i, r, g, b])
            wb.save("collected/datasheet2.xlsx")
        print(x,y)




