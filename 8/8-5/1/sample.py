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
        approx_curves = []
        for contour in contours:
            approx_curve = cv2.approxPolyDP(contour, 1, True)
            approx_curves.append(approx_curve)
        cv2.drawContours(gray, approx_curves, -1, (0, 0, 255))
        cv2.imshow('Contours', gray)

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
