import cv2
import numpy as np
image= cv2.imread(r'H:\SPEAMMMM\TikTok\try 2\test image\5.png')
# cv2.imshow('The img', image)
# cv2.waitKey(0)
template= cv2.imread(r'H:\SPEAMMMM\TikTok\try 2\test image\search_for\1.png',0)

def find_temp_in_img(template,image):
    

    gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result= cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(result)

    height, width= template.shape[:2]


    top_left= max_loc
    bottom_right= (top_left[0] + width, top_left[1] + height)
    cv2.rectangle(image, top_left, bottom_right, (0,0,255),5)
    print(top_left[0] + width , top_left[1] )
    return top_left[0] + width , top_left[1] 

print(find_temp_in_img(template,image))

cv2.imshow('Found', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

