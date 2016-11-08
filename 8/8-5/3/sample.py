# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

img = None
point = None

def onTrackbarSlide(pos):
    global img, point
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    ret, dst = cv2.threshold(gray, int(pos), 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    if contours:
        nomal_curves = []
        selected_curves = []
        if point != None:
            for contour in contours:
                if cv2.pointPolygonTest(contour, point, False) > 0:
                    selected_curves.append(contour)
                else:
                    nomal_curves.append(contour)
        else:
            nomal_curves = contours
        color = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
        cv2.drawContours(color, nomal_curves, -1, (0, 0, 0))
        cv2.drawContours(color, selected_curves, -1, (0, 0, 255))
        cv2.imshow('Contours', color)

def onClick(event, x, y, flags, param):
    global point
    if (event == 4):
        point = (x, y)
        onTrackbarSlide(cv2.getTrackbarPos('Threshold', 'Contours'))

def main(args):
    global img
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    cv2.namedWindow('Contours')
    cv2.createTrackbar('Threshold', 'Contours', 100, 255, onTrackbarSlide)
    cv2.setMouseCallback('Contours', onClick)
    cv2.imshow('Contours', img)

    onTrackbarSlide(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
