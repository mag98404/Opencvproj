import cv2 as cv
import numpy as np
import mss

template_image = cv.imread("cabbage.png", cv.IMREAD_UNCHANGED)

def get_template():
    return template_image

def grab_screen(region=None):
    with mss.mss() as sct:
        monitor = region if region else sct.monitors[2]
        sct_img = sct.grab(monitor)
        frame = np.array(sct_img)
       # frame = cv.cvtColor(frame, cv.COLOR_BGRA2BGR)
        return frame
    
