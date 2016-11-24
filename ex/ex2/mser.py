# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def onTrackbarSlide(pos):
    global img
    h, w = img.shape[:2]
    imgArea = h * w

    delta = cv2.getTrackbarPos('delta', 'Original')
    minArea = int(imgArea * 0.1 * cv2.getTrackbarPos('minArea', 'Original') / 100)
    maxArea = int(imgArea * 0.1 * cv2.getTrackbarPos('maxArea', 'Original') / 100)
    maxVariation = float(cv2.getTrackbarPos('maxVariation', 'Original')) / 100
    minDiversity = float(cv2.getTrackbarPos('minDiversity', 'Original')) / 100
    maxEvolution = cv2.getTrackbarPos('maxEvolution', 'Original') * 10
    areaThreshold = 1.0 + float(cv2.getTrackbarPos('areaThreshold', 'Original')) / 100
    minMargin = cv2.getTrackbarPos('minMargin', 'Original') / 1000
    edgeBlurSize = cv2.getTrackbarPos('edgeBlurSize', 'Original') * 2 + 3

    vis = img.copy()
    mser = cv2.MSER(delta, minArea, maxArea, maxVariation, minDiversity, maxEvolution, areaThreshold, minMargin, edgeBlurSize)
    regions = mser.detect(img, None)
    hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
    cv2.polylines(vis, hulls, 1, (0, 255, 0))
    cv2.imshow('Keypoints', vis)

def main(args):
    global img
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    h, w = img.shape[:2]
    img = cv2.resize(img, (int(w / 4), int(h / 4)))

    cv2.namedWindow('Original')
    cv2.namedWindow('Keypoints')

    cv2.createTrackbar('delta', 'Original', 10, 255, onTrackbarSlide)
    cv2.createTrackbar('minArea', 'Original', 10, 100, onTrackbarSlide)
    cv2.createTrackbar('maxArea', 'Original', 20, 100, onTrackbarSlide)
    cv2.createTrackbar('maxVariation', 'Original', 25, 100, onTrackbarSlide)
    cv2.createTrackbar('minDiversity', 'Original', 20, 100, onTrackbarSlide)
    cv2.createTrackbar('maxEvolution', 'Original', 20, 100, onTrackbarSlide)
    cv2.createTrackbar('areaThreshold', 'Original', 1, 100, onTrackbarSlide)
    cv2.createTrackbar('minMargin', 'Original', 3, 100, onTrackbarSlide)
    cv2.createTrackbar('edgeBlurSize', 'Original', 1, 10, onTrackbarSlide)

    cv2.imshow('Original', img)

    onTrackbarSlide(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
