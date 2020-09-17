import os
import openpyxl
from PIL import Image

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["대 카테고리", "세부 카테고리", "제품 번호", "R", "G", "B"])
print("새로 파일을 만들었습니다")

lst = [8, 18, 3, 6, 2]
for i in range(5):
    for j in range(lst[i] + 1):
        imageNum = os.walk('collected/image/' + str(i) + '/' + str(j)).__next__()[2]
        for k in range(len(imageNum)-1):
            image = Image.open('collected/image/' + str(i) + '/' + str(j) + '/' + str(k) + '.png')
            image = image.convert('RGB')
            if i==3:
                r, g, b = image.getpixel((62, 21))
            else:
                r, g, b = image.getpixel((62, 62))
            print(r, g, b)
            sheet.append([i, j, k, r, g, b])

wb.save("collected/color.xlsx")
