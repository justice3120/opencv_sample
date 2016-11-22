# -*- coding: utf-8 -*-

import sys
import os
import glob
import uuid
import shutil
import random
import numpy as np
import cv2

args = sys.argv

input_dir = '/tmp/opencv'
result_dir = '/tmp/opencv/result'

if os.path.isdir(result_dir):
    shutil.rmtree(result_dir)

em = cv2.EM(2)

files = glob.glob(input_dir + '/*.jpg')
files = random.sample(files, 10)

print 'Input Files: ' + str(len(files))

samples = []
for f in files:
    gray = cv2.cvtColor(cv2.imread(f), cv2.COLOR_RGB2GRAY)
    h, w = gray.shape[:2]
    gray = cv2.resize(gray, (int(w / 4), int(h / 4)))
    h, w = gray.shape[:2]
    sample = gray.reshape((h * w))
    samples.append(sample.copy())

print 'EM Start'
retval, logLikelihoods, labels, probs = em.train(np.asarray(samples))
print 'EM End'

if not os.path.isdir(result_dir):
    os.mkdir(result_dir)

for sample in samples:
    retval, probs = em.predict(sample)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(probs)
    class_num = str(max_loc[0])
    if not os.path.isdir(os.path.join(result_dir, class_num)):
        os.mkdir(os.path.join(result_dir, class_num))
    gray = sample.reshape((h, w))
    file_name = str(uuid.uuid4()) + '.jpg'
    cv2.imwrite(os.path.join(result_dir, class_num, file_name), gray)
