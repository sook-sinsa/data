from PIL import Image
import os

lst = [8, 18, 3, 6, 2]
for i in range(5):
    for j in range(lst[i] + 1):
        imageNum = os.walk('collected/image/' + str(i) + '/' + str(j)).__next__()[2]
        for k in range(len(imageNum)-1):
            image = Image.open('collected/image/' + str(i) + '/' + str(j) + '/' + str(k) + '.png')
            resizeImg = image.resize((125, 125))
            resizeImg.save('collected/image/' + str(i) + '/' + str(j) + '/' + str(k) + '.png')
