# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

args = sys.argv

cv2.namedWindow('Example2', cv2.WINDOW_AUTOSIZE)
capture = cv2.VideoCapture(args[1])

while(capture.isOpened()):
    ret, frame = capture.read()
    #if not frame:
    #  break
    cv2.imshow('Example2', frame)
    c = cv2.waitKey(33)
    if c == 27:
        break

capture.release()
cv2.destroyWindow('Example2')
