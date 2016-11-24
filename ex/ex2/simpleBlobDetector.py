# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def onTrackbarSlide(pos):
    global img
    params = cv2.SimpleBlobDetector_Params()
    params.minThreshold = cv2.getTrackbarPos('minThreshold', 'Original')
    params.maxThreshold = cv2.getTrackbarPos('maxThreshold', 'Original')
    params.filterByArea = True
    h, w = img.shape[:2]
    params.minArea = (h * w * cv2.getTrackbarPos('minArea', 'Original')) / 10000
    params.filterByCircularity = True
    params.minCircularity = float(cv2.getTrackbarPos('minCircularity', 'Original')) / 100
    params.filterByConvexity = True
    params.minConvexity = float(cv2.getTrackbarPos('minConvexity', 'Original')) / 100
    params.filterByInertia = True
    params.minInertiaRatio = float(cv2.getTrackbarPos('minInertiaRatio', 'Original')) / 100

    detector = cv2.SimpleBlobDetector(params)
    keypoints = detector.detect(img)
    im_with_keypoints = cv2.drawKeypoints(img.copy(), keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow('Keypoints', im_with_keypoints)

def main(args):
    global img
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1], cv2.IMREAD_GRAYSCALE)
    h, w = img.shape[:2]
    img = cv2.resize(img, (int(w / 4), int(h / 4)))

    cv2.namedWindow('Original')
    cv2.namedWindow('Keypoints')

    cv2.createTrackbar('minThreshold', 'Original', 10, 255, onTrackbarSlide)
    cv2.createTrackbar('maxThreshold', 'Original', 200, 255, onTrackbarSlide)
    cv2.createTrackbar('minArea', 'Original', 10, 100, onTrackbarSlide)
    cv2.createTrackbar('minCircularity', 'Original', 10, 100, onTrackbarSlide)
    cv2.createTrackbar('minConvexity', 'Original', 87, 100, onTrackbarSlide)
    cv2.createTrackbar('minInertiaRatio', 'Original', 1, 100, onTrackbarSlide)

    cv2.imshow('Original', img)

    onTrackbarSlide(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
