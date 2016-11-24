# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def onTrackbarSlide(pos):
    global img
    h, w = img.shape[:2]
    imgArea = h * w

    nfeatures = int(cv2.getTrackbarPos('nfeatures', 'Original') * 10)
    scaleFactor = 1.0 + float(cv2.getTrackbarPos('scaleFactor', 'Original')) / 100.0
    nlevels = int(cv2.getTrackbarPos('nlevels', 'Original'))
    edgeThreshold = int(cv2.getTrackbarPos('edgeThreshold', 'Original'))
    firstLevel = 0
    k = cv2.getTrackbarPos('WTA_K', 'Original')
    patchSize = int(cv2.getTrackbarPos('patchSize', 'Original'))

    vis = img.copy()
    orb = cv2.ORB(nfeatures, scaleFactor, nlevels, edgeThreshold, firstLevel, k, cv2.ORB_FAST_SCORE, patchSize)
    keypoints = orb.detect(img, None)
    im_with_keypoints = cv2.drawKeypoints(img.copy(), keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('Keypoints FAST_SCORE', im_with_keypoints)

    orb = cv2.ORB(nfeatures, scaleFactor, nlevels, edgeThreshold, firstLevel, k, cv2.ORB_HARRIS_SCORE, patchSize)
    keypoints = orb.detect(img, None)
    im_with_keypoints = cv2.drawKeypoints(img.copy(), keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('Keypoints HARRIS_SCORE', im_with_keypoints)

def main(args):
    global img
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    h, w = img.shape[:2]
    img = cv2.resize(img, (int(w / 4), int(h / 4)))

    cv2.namedWindow('Original')
    cv2.namedWindow('Keypoints FAST_SCORE')
    cv2.namedWindow('Keypoints HARRIS_SCORE')

    cv2.createTrackbar('nfeatures', 'Original', 50, 100, onTrackbarSlide)
    cv2.createTrackbar('scaleFactor', 'Original', 20, 100, onTrackbarSlide)
    cv2.createTrackbar('nlevels', 'Original', 8, 100, onTrackbarSlide)
    cv2.createTrackbar('edgeThreshold', 'Original', 31, 100, onTrackbarSlide)
    cv2.createTrackbar('WTA_K', 'Original', 2, 10, onTrackbarSlide)
    cv2.createTrackbar('patchSize', 'Original', 31, 100, onTrackbarSlide)

    cv2.imshow('Original', img)

    onTrackbarSlide(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
