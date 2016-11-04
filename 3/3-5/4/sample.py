# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def main(args):
    img = cv2.imread(args[1])
    cv2.putText(img, 'bird', (50, 50), cv2.FONT_HERSHEY_COMPLEX , 1, (0, 0, 255))
    cv2.namedWindow('Window')
    cv2.imshow('Window', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

if __name__ == '__main__':
    args = sys.argv
    main(args)
