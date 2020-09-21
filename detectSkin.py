import numpy as np
import cv2

def tracking():
    image_path = './test3.png'
    img = cv2.imread(image_path)

    lower_green = np.array([255, 223, 196])
    upper_green = np.array([229, 194, 152])

    while True:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        green_range = cv2.inRange(hsv, lower_green, upper_green)
        green_result = cv2.bitwise_and(img, img, mask=green_range)
        

        cv2.imshow("original", img)
        cv2.imshow("green", green_result)

        cv2.imwrite('./detectSkin-result.png', green_result)
        key = cv2.waitKey(1) & 0xFF 
        if key == 27: 
            break 
    cv2.destroyAllWindows()

tracking()
