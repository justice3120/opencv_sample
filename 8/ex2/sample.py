# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

img = None
gray = None
rgb_gray = None

def onTrackbarSlide(pos):
    global gray, rgb_gray
    printContours('Contours', gray)
    printContours('Contours RGB', rgb_gray)

def printContours(window, img):
    #ret, dst = cv2.threshold(gray, int(pos), 255, cv2.THRESH_BINARY)
    low = cv2.getTrackbarPos('Low', 'Contours')
    high = cv2.getTrackbarPos('High', 'Contours')
    dst = cv2.Canny(img, low, high)
    contours, hierarchy = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    if contours:
        color = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        cv2.drawContours(color, contours, -1, (0, 0, 255))
        cv2.imshow(window, color)

def main(args):
    global img, gray, rgb_gray
    if len(args) != 2:
        return -1
    img = cv2.pyrDown(cv2.imread(args[1]))
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    rgb = cv2.split(img)
    rgb_gray = cv2.max(cv2.max(rgb[2], rgb[1]), rgb[0])

    cv2.namedWindow('Contours')
    cv2.createTrackbar('Low', 'Contours', 10, 255, onTrackbarSlide)
    cv2.createTrackbar('High', 'Contours', 100, 255, onTrackbarSlide)
    cv2.namedWindow('Contours RGB')

    onTrackbarSlide(100)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
