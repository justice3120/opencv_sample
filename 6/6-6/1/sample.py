# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def onTrackbarSlide(pos):
    global gray, canny
    rho = cv2.getTrackbarPos('rho', 'Original') + 1
    theta = np.radians((cv2.getTrackbarPos('theta', 'Original') * 10 + 10))
    threshold = cv2.getTrackbarPos('threshold', 'Original') + 1

    lines  = cv2.HoughLines(canny, rho, theta, threshold)
    # cv2.imshow('Tresh 2:1', dst)
    lines  = cv2.HoughLinesP(canny, rho, theta, threshold)
    ppht = cv2.cvtColor(gray.copy(), cv2.COLOR_GRAY2RGB)
    if lines != None:
        for line in lines[0,0:]:
            cv2.line(ppht, tuple(line[0:2]), tuple(line[2:4]), (0, 0, 255), 3)
    cv2.imshow('PPHT', ppht)

def main(args):
    global gray, canny
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    h, w = img.shape[:2]
    img = cv2.resize(img, (int(w / 4), int(h / 4)))
    gray = cv2.cvtColor(img.copy(), cv2.COLOR_RGB2GRAY)
    canny = cv2.Canny(gray.copy(), 50, 150)

    cv2.namedWindow('Original')
    cv2.namedWindow('SHT')
    cv2.namedWindow('PPHT')

    cv2.createTrackbar('rho', 'Original', 0, 100, onTrackbarSlide)
    cv2.createTrackbar('theta', 'Original', 0, 35, onTrackbarSlide)
    cv2.createTrackbar('threshold', 'Original', 0, 1000, onTrackbarSlide)

    cv2.imshow('Original', gray)

    onTrackbarSlide(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
