# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def onTrackbarSlide(pos):
    global gray
    dp = cv2.getTrackbarPos('dp', 'Original') + 1
    minDist = cv2.getTrackbarPos('minDist', 'Original') + 1

    circles  = cv2.HoughCircles(gray.copy(), cv2.cv.CV_HOUGH_GRADIENT, dp, minDist)
    print circles
    # ppht = cv2.cvtColor(gray.copy(), cv2.COLOR_GRAY2RGB)
    # if circles != None:
    #     for line in lines[0,0:]:
    #         cv2.line(ppht, tuple(line[0:2]), tuple(line[2:4]), (0, 0, 255), 3)
    # cv2.imshow('HoughCircles', ppht)

def main(args):
    if len(args) != 2:
        return -1
    dp = 1
    minDist = 30
    param1 = 50
    param2 = 150
    minRadius = 5
    maxRadius = 10

    img = cv2.imread(args[1])
    h, w = img.shape[:2]
    img = cv2.resize(img, (int(w / 4), int(h / 4)))
    gray = cv2.cvtColor(img.copy(), cv2.COLOR_RGB2GRAY)

    cv2.namedWindow('Original')
    cv2.namedWindow('HoughCircles')

    cv2.imshow('Original', gray)

    circles  = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, dp, minDist, param1, param2, minRadius, maxRadius)
    hc = cv2.cvtColor(gray.copy(), cv2.COLOR_GRAY2RGB)
    if circles != None:
        for circle in circles[0,0:]:
            cv2.circle(hc, tuple(circle[0:2]), circle[2], (0, 0, 255), 1)
    cv2.imshow('HoughCircles', hc)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
