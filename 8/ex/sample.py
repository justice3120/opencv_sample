# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

img = None
img2 = None
gray = None
gray2 = None
contours = []
contours2 = []
point = (0, 0)
epsilon = 0.0
size_rate = 0.1
match_shape_thr = 0.1

def onTrackbarSlide(pos):
    global img1, img2, gray, gray2, point, contours, contours2
    ret, dst = cv2.threshold(gray, int(pos), 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    ret2, dst2 = cv2.threshold(gray2, int(pos), 255, cv2.THRESH_BINARY)
    contours2, hierarchy2 = cv2.findContours(dst2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    update()

def onSizeTrackbarSlide(pos):
    global size_rate
    size_rate = pos
    update()

def onEpsilonTrackbarSlide(pos):
    global epsilon
    epsilon = pos / 10
    update()

def onMatchShapeTrackbarSlide(pos):
    global match_shape_thr
    match_shape_thr = pos / 10
    update()

def onMouse(event, x, y, flags, param):
    global point
    if (event == 4):
        point = (x * 2, y * 2)
        update()

def update():
    global gray, gray2, point, contours, contours2, epsilon, size_rate, match_shape_thr
    approx_contours = approxCurves(contours, epsilon)
    approx_contours2 = approxCurves(contours2, epsilon)

    selected_curve = getSelectedCurve(approx_contours, point)
    size_filterd_curves = filterByCurveSize(approx_contours2, selected_curve)

    i1_matched_curves = []
    i2_matched_curves = []
    i3_matched_curves = []
    for contour in size_filterd_curves:
        if cv2.matchShapes(contour, selected_curve, cv2.cv.CV_CONTOURS_MATCH_I1, 0) < match_shape_thr:
            i1_matched_curves.append(contour)
        if cv2.matchShapes(contour, selected_curve, cv2.cv.CV_CONTOURS_MATCH_I2, 0) < match_shape_thr:
            i2_matched_curves.append(contour)
        if cv2.matchShapes(contour, selected_curve, cv2.cv.CV_CONTOURS_MATCH_I3, 0) < match_shape_thr:
            i3_matched_curves.append(contour)

    color = cv2.pyrDown(cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB))
    cv2.drawContours(color, resizeCurves(approx_contours, 0.5), -1, (0, 0, 0))
    cv2.drawContours(color, resizeCurves([selected_curve], 0.5), -1, (0, 0, 255))
    cv2.imshow('Contours', color)

    i1_matched = cv2.pyrDown(cv2.cvtColor(gray2, cv2.COLOR_GRAY2RGB))
    cv2.drawContours(i1_matched, resizeCurves(approx_contours2, 0.5), -1, (0, 0, 0))
    cv2.drawContours(i1_matched, resizeCurves(i1_matched_curves, 0.5), -1, (0, 0, 255))
    cv2.imshow('I1 Matched', i1_matched)

    i2_matched = cv2.pyrDown(cv2.cvtColor(gray2, cv2.COLOR_GRAY2RGB))
    cv2.drawContours(i2_matched, resizeCurves(approx_contours2, 0.5), -1, (0, 0, 0))
    cv2.drawContours(i2_matched, resizeCurves(i2_matched_curves, 0.5), -1, (0, 0, 255))
    cv2.imshow('I2 Matched', i2_matched)

    i3_matched = cv2.pyrDown(cv2.cvtColor(gray2, cv2.COLOR_GRAY2RGB))
    cv2.drawContours(i3_matched, resizeCurves(approx_contours2, 0.5), -1, (0, 0, 0))
    cv2.drawContours(i3_matched, resizeCurves(i3_matched_curves, 0.5), -1, (0, 0, 255))
    cv2.imshow('I3 Matched', i3_matched)

    return

def getSelectedCurve(contours, point):
    selected_curve = None
    selected_curve_distance = None
    for contour in contours:
        if selected_curve_distance == None:
            selected_curve = contour
            selected_curve_distance = cv2.pointPolygonTest(contour, point, True)
        else:
            distance = cv2.pointPolygonTest(contour, point, True)
            if abs(selected_curve_distance) > abs(distance):
                selected_curve = contour
                selected_curve_distance = distance
    return selected_curve

def filterByCurveSize(contours, selected_curve):
    size_filterd_curves = []
    selected_curve_area = cv2.contourArea(selected_curve)
    min_area = selected_curve_area * (100 - size_rate) / 100
    max_area = selected_curve_area * (100 + size_rate) / 100
    for contour in contours:
        area = cv2.contourArea(contour)
        if min_area <= area and area <= max_area:
            size_filterd_curves.append(contour)
    return size_filterd_curves

def approxCurves(curves, epsilon):
    approxed_curves = []
    for curve in curves:
        approxed_curves.append(cv2.approxPolyDP(curve, epsilon, True))
    return approxed_curves

def resizeCurves(curves, rate):
    resized_curves = []
    for curve in curves:
        resized_curve = curve * rate
        resized_curves.append(resized_curve.astype(np.int32))
    return resized_curves

def main(args):
    global img, img2, gray, gray2
    if len(args) != 3:
        return -1
    img = cv2.imread(args[1])
    img = cv2.resize(img, (img.shape[1] / 2, img.shape[0] / 2))
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    img2 = cv2.imread(args[2])
    img2 = cv2.resize(img2, (int(img2.shape[1] / 1.5), int(img2.shape[0] / 1.5)))
    gray2 = cv2.cvtColor(np.array(img2), cv2.COLOR_RGB2GRAY)

    cv2.namedWindow('Contours')
    cv2.namedWindow('I1 Matched')
    cv2.moveWindow('I1 Matched', img.shape[1] / 2 + 10, 0)
    cv2.namedWindow('I2 Matched')
    cv2.moveWindow('I2 Matched', img.shape[1] / 2 + img2.shape[1] / 2 + 20, 0)
    cv2.namedWindow('I3 Matched')
    cv2.moveWindow('I3 Matched', img.shape[1] / 2 + img2.shape[1] + 30, 0)
    cv2.createTrackbar('Threshold', 'Contours', 100, 255, onTrackbarSlide)
    cv2.createTrackbar('Poly Epsilon', 'Contours', 0, 100, onEpsilonTrackbarSlide)
    cv2.createTrackbar('Size Rate', 'Contours', 10, 100, onSizeTrackbarSlide)
    cv2.createTrackbar('Threshold for MatchShape', 'Contours', 10, 100, onMatchShapeTrackbarSlide)
    cv2.setMouseCallback('Contours', onMouse)
    cv2.imshow('Contours', img)

    onTrackbarSlide(100)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
