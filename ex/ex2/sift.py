# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def onTrackbarSlide(pos):
    global img
    h, w = img.shape[:2]
    imgArea = h * w

    nfeatures = int(cv2.getTrackbarPos('nfeatures', 'Original'))
    nOctaveLayers = int(cv2.getTrackbarPos('nOctaveLayers', 'Original'))
    contrastThreshold = float(cv2.getTrackbarPos('contrastThreshold', 'Original')) / 100.0
    edgeThreshold = int(cv2.getTrackbarPos('edgeThreshold', 'Original'))
    sigma = float(cv2.getTrackbarPos('sigma', 'Original')) / 10

    vis = img.copy()
    sift = cv2.SIFT(nfeatures, nOctaveLayers, contrastThreshold, edgeThreshold, sigma)
    keypoints = sift.detect(img, None)
    im_with_keypoints = cv2.drawKeypoints(img.copy(), keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('Keypoints', im_with_keypoints)

def main(args):
    global img
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    h, w = img.shape[:2]
    img = cv2.resize(img, (int(w / 4), int(h / 4)))

    cv2.namedWindow('Original')
    cv2.namedWindow('Keypoints')

    cv2.createTrackbar('nfeatures', 'Original', 0, 100, onTrackbarSlide)
    cv2.createTrackbar('nOctaveLayers', 'Original', 3, 10, onTrackbarSlide)
    cv2.createTrackbar('contrastThreshold', 'Original', 4, 100, onTrackbarSlide)
    cv2.createTrackbar('edgeThreshold', 'Original', 10, 100, onTrackbarSlide)
    cv2.createTrackbar('sigma', 'Original', 16, 100, onTrackbarSlide)

    cv2.imshow('Original', img)

    onTrackbarSlide(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
