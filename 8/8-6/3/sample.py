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
        selected_curve = None
        selected_curve_distance = None
        i1_matched_curves = []
        i2_matched_curves = []
        i3_matched_curves = []
        if point != None:
            for contour in contours:
                if selected_curve_distance == None:
                    selected_curve = contour
                    selected_curve_distance = cv2.pointPolygonTest(contour, point, True)
                else:
                    distance = cv2.pointPolygonTest(contour, point, True)
                    if abs(selected_curve_distance) > abs(distance):
                        nomal_curves.append(selected_curve)
                        selected_curve = contour
                        selected_curve_distance = distance
                    else:
                        nomal_curves.append(contour)

            for contour in contours:
                if cv2.matchShapes(contour, selected_curve, cv2.cv.CV_CONTOURS_MATCH_I1, 0) < 0.1:
                    i1_matched_curves.append(contour)
                if cv2.matchShapes(contour, selected_curve, cv2.cv.CV_CONTOURS_MATCH_I2, 0) < 0.1:
                    i2_matched_curves.append(contour)
                if cv2.matchShapes(contour, selected_curve, cv2.cv.CV_CONTOURS_MATCH_I3, 0) < 0.1:
                    i3_matched_curves.append(contour)
        else:
            nomal_curves = contours

        color = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
        cv2.drawContours(color, nomal_curves, -1, (0, 0, 0))
        cv2.drawContours(color, [selected_curve], -1, (0, 0, 255))
        cv2.imshow('Contours', color)

        i1_matched = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
        cv2.drawContours(i1_matched, i1_matched_curves, -1, (0, 0, 255))
        cv2.imshow('I1 Matched', i1_matched)

        i2_matched = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
        cv2.drawContours(i2_matched, i2_matched_curves, -1, (0, 0, 255))
        cv2.imshow('I2 Matched', i1_matched)

        i3_matched = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
        cv2.drawContours(i3_matched, i3_matched_curves, -1, (0, 0, 255))
        cv2.imshow('I3 Matched', i3_matched)

def onMouse(event, x, y, flags, param):
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
    cv2.namedWindow('I1 Matched')
    cv2.moveWindow('I1 Matched', img.shape[1], 0)
    cv2.namedWindow('I2 Matched')
    cv2.moveWindow('I2 Matched', img.shape[1] * 2, 0)
    cv2.namedWindow('I3 Matched')
    cv2.moveWindow('I3 Matched', img.shape[1] * 3, 0)
    cv2.createTrackbar('Threshold', 'Contours', 100, 255, onTrackbarSlide)
    cv2.setMouseCallback('Contours', onMouse)
    cv2.imshow('Contours', img)

    onTrackbarSlide(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
