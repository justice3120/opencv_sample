# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def main(args):
    img = cv2.imread(args[1])
    cv2.circle(img, (100, 100), 50, (0, 0, 255), 3)
    cv2.ellipse(img, (200, 200), (80, 40), -30, 0, 360, (255, 0, 0), 5)
    cv2.namedWindow('Window')
    cv2.imshow('Window', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

if __name__ == '__main__':
    args = sys.argv
    main(args)
