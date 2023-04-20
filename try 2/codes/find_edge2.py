import cv2
import numpy as np

def find_centroids(dst):
    ret, dst = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)
    dst = np.uint8(dst)

    # find centroids
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

    # define the criteria to stop and refine the corners
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

    return corners

# Read image of the widget
img = cv2.imread(r"H:\SPEAMMMM\TikTok\try 2\test image\3.png")

bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Convert to grayscale
gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

# Apply thresholding to segment the object
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Remove noise with morphological opening
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations = 2)

# Find contours of the object
ctrs, hier = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours by area
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.contourArea(ctr))

# Get bounding box coordinates for the largest contour (the object)
x, y, w, h = cv2.boundingRect(sorted_ctrs[-1])

# Draw bounding box on the image
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

# Display the image
cv2.imshow("Edges", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
