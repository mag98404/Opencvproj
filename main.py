import cv2 as cv
import numpy as np
import pyautogui
import time
from capture import grab_screen, get_template


template = cv.imread("cabbage.png", cv.IMREAD_UNCHANGED)

def findClickablePoints(target_image, map_image, threshold=0.7):
    '''
    #Load images
    map_image = cv.imread(map_image_path, cv.IMREAD_UNCHANGED)
    target_image = cv.imread(target_image_path, cv.IMREAD_UNCHANGED)

    if map_image is None or target_image is None:
     print("Error: Could not load images")
     exit()
    '''
#Template matching
    result = cv.matchTemplate(map_image, target_image, cv.TM_CCOEFF_NORMED)

#Threshold for declaring a match
    locations = np.where(result >= threshold)

#Get template size
    h, w = target_image.shape[:2]

    rectangles = []
    points = []

#Loop through all matches, add to rectangles array
    for pt in zip(*locations[::-1]):  # (x, y) points
     top_left = pt
     bottom_right = (pt[0] + w, pt[1] + h)
     rect = [pt[0], pt[1], w, h]
     rectangles.append(rect)
     rectangles.append(rect) #append twice for cases where there is only 1 rect on object

#Group rectangles together
    group_rect, rect_weights = cv.groupRectangles(rectangles, 1)

    line_color = (0,255,0)
    line_type = cv.LINE_4
    marker_color = (255, 0, 255)
    marker_type = cv.MARKER_CROSS


#Print rectangles
    for (x, y, w, h) in group_rect:

     center_x = x + int(w/2)
     center_y = y + int(h/2)

     points.append((int(center_x), int(center_y))) #Converted into int coordinates instead of np.int
     cv.drawMarker(map_image, (center_x, center_y), marker_color, marker_type)
     cv.rectangle(map_image, (x,y), (x + w, y + h), (0,0,255), 2)

    return points, map_image


prev_time = time.time()

while True:
  frame = grab_screen()
  points, after_image = findClickablePoints(template, frame)
  #print(points)
  cv.imshow("Detected Cabbages", after_image)
  
  curr_time = time.time()
  fps = 1 / (curr_time - prev_time)
  prev_time = curr_time
  print(f"FPS: {fps:.2f}")  # print to console


  if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()

''''
points, after_image = findClickablePoints("cabbage.png", "cabbage_patch.png")
print(points)
'''
'''
#Show result
cv.imshow("Detected Cabbages", after_image)
cv.waitKey(0)
'''

