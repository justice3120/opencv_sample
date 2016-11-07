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
        draw_curves = []
        for contour in contours:
            #boundingRect = cv2.boundingRect(contour)
            #rest_points = getPointsFromBoundingRect(boundingRect)
            minAreaRect = cv2.minAreaRect(contour)
            rest_points = getPointsMinAreaRect(minAreaRect)
            draw_curves.append(rest_points)
        cv2.drawContours(gray, draw_curves, -1, (0, 0, 255))
        cv2.imshow('Contours', gray)

def getPointsFromBoundingRect(boundingRect):
    r = boundingRect
    points = np.asarray([[[
        r[0], r[1]
    ]], [[
        r[0] + r[2], r[1]
    ]], [[
        r[0] + r[2], r[1] + r[3]
    ]], [[
        r[0], r[1] + r[3]
    ]]])
    return points

def getPointsMinAreaRect(minAreaRect):
    r = minAreaRect
    x, y = r[0]
    w, h = r[1]
    rad = np.deg2rad(r[2])
    points = np.asarray([[[
        int(x - (w * np.cos(rad) - h * np.sin(rad)) / 2), int(y + (w * np.sin(rad) + h * np.cos(rad)) / 2)
    ]], [[
        int(x + (w * np.cos(rad) + h * np.sin(rad)) / 2), int(y + (- w * np.sin(rad) + h * np.cos(rad)) / 2)
    ]], [[
        int(x + (w * np.cos(rad) - h * np.sin(rad)) / 2), int(y - (w * np.sin(rad) + h * np.cos(rad)) / 2)
    ]], [[
        int(x - (w * np.cos(rad) + h * np.sin(rad)) / 2), int(y - (- w * np.sin(rad) + h * np.cos(rad)) / 2)
    ]]])
    return points

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
