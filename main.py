import cv2 as cv
import numpy as np

#Load images
cabbage_patch = cv.imread("cabbage_patch.png", cv.IMREAD_UNCHANGED)
cabbage = cv.imread("cabbage.png", cv.IMREAD_UNCHANGED)

if cabbage_patch is None or cabbage is None:
    print("Error: Could not load images")
    exit()

#Template matching
result = cv.matchTemplate(cabbage_patch, cabbage, cv.TM_CCOEFF_NORMED)

#Threshold for declaring a match
threshold = 0.56
locations = np.where(result >= threshold)

#Get template size
h, w = cabbage.shape[:2]

rectangles = []

#Loop through all matches, add to rectangles array
for pt in zip(*locations[::-1]):  # (x, y) points
    top_left = pt
    bottom_right = (pt[0] + w, pt[1] + h)
    rect = [pt[0], pt[1], w, h]
    rectangles.append(rect)
    rectangles.append(rect) #append twice for cases where there is only 1 rect on object

#Group rectangles together
group_rect, rect_weights = cv.groupRectangles(rectangles, 1)

#Print rectangles
for (x, y, w, h) in group_rect:
    cv.rectangle(cabbage_patch, (x,y), (x + w, y + h), (0,0,255), 2)



#Show result
cv.imshow("Detected Cabbages", cabbage_patch)
cv.waitKey(0)
