# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

args = sys.argv

img = cv2.imread(args[1])
cv2.namedWindow('Example1', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Example1', img)
cv2.waitKey(0)
cv2.destroyWindow('Example1')
