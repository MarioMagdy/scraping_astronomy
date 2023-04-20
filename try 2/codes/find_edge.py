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

# Read image of the object
img = cv2.imread(r"H:\SPEAMMMM\TikTok\try 2\test image\2.png")
bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Convert to grayscale
gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

# Convert to uint8
gray = np.uint8(gray)

# Apply Harris corner detection
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)

# Get corner coordinates
corners= find_centroids(dst)

# Draw corners on the image
for corner in corners:
    img[int(corner[1]), int(corner[0])] = [0, 0, 255]

# Find contours of the edges
ctrs, hier = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours by area
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.contourArea(ctr))

# Get bounding box coordinates for each contour
for i, ctr in enumerate(sorted_ctrs):
    x, y, w, h = cv2.boundingRect(ctr)

    # Draw bounding box on the image
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

# Display the image
cv2.imshow("Edges", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
