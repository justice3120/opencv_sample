# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def main(args):
    img = cv2.imread(args[1])
    points = np.array([[10, 10], [125, 25], [30, 55], [50, 10]])
    cv2.fillPoly(img, [points], (0, 0, 255))
    cv2.fillConvexPoly(img, points + 100, (255, 0, 0))
    cv2.polylines(img, [points + [200, 0]], True, (0, 255, 0), 1, 16)
    cv2.namedWindow('Window')
    cv2.imshow('Window', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

if __name__ == '__main__':
    args = sys.argv
    main(args)
