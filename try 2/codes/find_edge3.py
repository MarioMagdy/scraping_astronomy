import cv2 
import numpy as np

def find_centroids(dst):
    ret, dst = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)
    dst = np.uint8(dst) 
    # rest of function...

# Read image of the object 
img = cv2.imread(r"H:\SPEAMMMM\TikTok\try 2\test image\2.png")
cv2.imshow("img", img)
bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Convert to grayscale 
gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

# Apply threshold to get binary image
ret, thresh = cv2.threshold(gray,50, 70, 0)

# Find contours 
ctrs, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Rest of code...


# Sort contours by area
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.contourArea(ctr))

# Get bounding box coordinates for each contour
for i, ctr in enumerate(sorted_ctrs):
    x, y, w, h = cv2.boundingRect(ctr)

    # Draw bounding box on the image
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

# Display the image


print(x + w, y) 

print(sorted_ctrs[-1]) 


cv2.imshow("Edges", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
