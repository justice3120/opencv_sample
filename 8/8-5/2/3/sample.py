# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

img = None
gray = None

def onTrackbarSlide(pos):
    global img
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    ret, dst = cv2.threshold(gray, int(pos), 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    if contours:
        copy_gray = np.array(gray)
        for contour in contours:
            #center, radius = cv2.minEnclosingCircle(contour)
            #cv2.circle(copy_gray, (int(center[0]), int(center[1])), int(radius), (0, 0, 255), 1)
            if len(contour) >= 5:
                ellipse = cv2.fitEllipse(contour)
                cv2.ellipse(copy_gray, ellipse, (0, 0, 255), 1)
        cv2.imshow('Contours', copy_gray)

def main(args):
    global img
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    cv2.namedWindow('Contours')
    cv2.createTrackbar('Threshold', 'Contours', 100, 255, onTrackbarSlide)
    cv2.imshow('Contours', img)

    onTrackbarSlide(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
