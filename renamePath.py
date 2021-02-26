# train dataset :
# /content/drive/My Drive/Colab Notebooks/yolact-master/data/test/파일이름.png
#
# validation dataset:
# /content/drive/My Drive/Colab Notebooks/yolact-master/data/validation/파일이름.png
#
# 로컬 경로
# train:
# "C:/Users/LG/Desktop/cocodataset_before/test\\파일이름.png"
#
# validation:
# C:/Users/LG/Desktop/cocodataset_before/validation\\파일이름.png

import json
import os
from os import rename

with open('clothes/train.json', 'r') as f:
    jsonData = json.load(f)
imgList = jsonData['images']
for i in range(144*4) :
    path = jsonData['images'][i]['file_name']
    print(path)
    imgName = path.split('\\')[-1]
    print(imgName)
    colabPath = "/content/drive/My Drive/Colab Notebooks/yolact-master/data/train/" + imgName
    jsonData['images'][i]['file_name'] = colabPath

    with open('clothes/train.json', 'w', encoding='utf-8') as make_file:
        json.dump(jsonData, make_file, indent="\t")
