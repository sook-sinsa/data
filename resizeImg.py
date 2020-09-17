import os
import shutil

bigCategory = int(input("Input Big Category Number(0-4) : "))
smallCategory = int(input("Input Small Category Number : "))

img_dir = './collected/image/'+str(bigCategory)+'/'+str(smallCategory)

print(len(os.listdir(img_dir)))
#print(os.listdir(img_dir))

from keras.preprocessing import image

for i in range(len(os.listdir(img_dir))-1):
    img_path = os.path.join(img_dir,str(i)+'.png')
    img = image.load_img(img_path, target_size=(125, 125))
    img_array = image.img_to_array(img)
    image.save_img(img_path, img_array)