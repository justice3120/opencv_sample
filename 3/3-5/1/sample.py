# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def main(args):
    img = cv2.imread(args[1])
    cv2.line(img, (0, 0), (100, 100), (0, 0, 255), 3)
    cv2.rectangle(img, (0, 10), (30, 50), (255, 0, 0), 5)
    cv2.namedWindow('Window')
    cv2.imshow('Window', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

if __name__ == '__main__':
    args = sys.argv
    main(args)
