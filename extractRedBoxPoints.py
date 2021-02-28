import os
from PIL import Image
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["카테고리","제품번호", "point-1","point-2","point-3","point-4"])
print("새로 파일을 만들었습니다.")

itemCategory = ['collar','hood','ssleeve','nsleeve','lsleeve']

#    [0,1,2,3,4,5],
#    [0,1],
#    [0,1],
#    [0]

# 이 부분과 아래 range 부분을 적절하게 수정해서 사용해주세요!


for i in range(len(itemCategory)):
    bigCategory = itemCategory[i]
    #for j in range(len(itemCategory[i])):
    #   smallCategory = j

    img_dir = './'+str(bigCategory)+'_red'
        #os.mkdir(img_dir+'/crop')

    for itemNum in range(len(os.listdir(img_dir))):
        img_path = os.path.join(img_dir,str(itemNum)+'.png')
        image = Image.open(img_path)
        image = image.convert('RGB')
        arr = []
        for x in range(125):
            for y in range(125):
                if (image.getpixel((x,y))==(244, 67, 54)):
                    arr.append((x, y))

        x1, y1 = arr[0]

        testx = x1+20

        yi = y1
        height=0

        while True:
            if(image.getpixel((testx, yi)) !=(244,67,54)):
                break;
            yi += 1
            height += 1

        y1 = y1 + height -1 # 라벨 칸 만큼 내리기

        arr.sort(key=lambda i : (i[1], i[0])) # y좌표 오름차순 정렬 -> x좌표 오름차순 정렬
        x2, y2 = arr[len(arr)-1]

        # area = (x1+1, y1+1, x2,y2)
        #
        # crop_image = image.crop(area)
        # crop_path = os.path.join(img_dir,'crop',str(itemNum)+'.png')
        # crop_image.save(crop_path)

        originImg = Image.open('./'+str(bigCategory)+'/' + str(itemNum) + '.png')
        originImg = originImg.convert('RGB')

        originImg.save('./'+str(bigCategory)+'/' + str(itemNum) + '.png')

        sheet.append([bigCategory, itemNum, x1+1, y1+1, x2, y2])
        wb.save("datasheetColor.xlsx")

            
    print("====================")
    print("완료 카테고리 :",itemCategory[i])