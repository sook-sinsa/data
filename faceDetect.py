import cv2

fileName=r"./big-img.png"
img_src=cv2.imread(fileName)

img = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
img2 = img_src

cascade_fillename = r"./haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_fillename)

face_data = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=1, minSize=(70,70))

cv2.namedWindow("image viewer1", cv2.WINDOW_NORMAL)
cv2.imshow("image viewer1", img_src)

if len(face_data) > 0:
    color = (255,0,255)
    for f in face_data:
        x, y, w, h = f
        cv2.rectangle(img2, (x,y), (x+w, y+h), color, -1)
    
    cv2.namedWindow("image viewer2", cv2.WINDOW_NORMAL)
    cv2.imshow("image viewer2", img2)

    cv2.imwrite(r"./big-list.png", img2)
else:
    print("not found")

cv2.waitKey(10000)
cv2.destroyAllWindows()