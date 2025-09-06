import cv2 as cv
import numpy as np

#Import images
cabbage_patch = cv.imread("cabage_patch.png", cv.IMREAD_UNCHANGED)
cabbage = cv.imread("cabbage.png", cv.IMREAD_UNCHANGED)

#Computer vision
result = cv.matchTemplate(cabbage_patch, cabbage, cv.TM_CCOEFF_NORMED)

#Opening resulting cv image for debugging
cv.imshow("result", result)
cv.waitKey()