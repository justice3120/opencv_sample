# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def onTrackbarSlide(pos):
    global img
    h, w = img.shape[:2]
    imgArea = h * w

    hessianThreshold = float(cv2.getTrackbarPos('hessianThreshold', 'Original')) / 10
    nOctaves = int(cv2.getTrackbarPos('nOctaves', 'Original'))
    nOctaveLayers = int(cv2.getTrackbarPos('nOctaveLayers', 'Original'))
    extended = bool(cv2.getTrackbarPos('extended', 'Original'))
    upright = bool(cv2.getTrackbarPos('upright', 'Original'))

    vis = img.copy()
    surf = cv2.SURF(hessianThreshold, nOctaves, nOctaveLayers, extended, upright)
    keypoints = surf.detect(img, None)
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

    cv2.createTrackbar('hessianThreshold', 'Original', 0, 100, onTrackbarSlide)
    cv2.createTrackbar('nOctaves', 'Original', 4, 10, onTrackbarSlide)
    cv2.createTrackbar('nOctaveLayers', 'Original', 2, 10, onTrackbarSlide)
    cv2.createTrackbar('extended', 'Original', 1, 1, onTrackbarSlide)
    cv2.createTrackbar('upright', 'Original', 0, 1, onTrackbarSlide)

    cv2.imshow('Original', img)

    onTrackbarSlide(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
