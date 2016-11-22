# -*- coding: utf-8 -*-

import sys
import os
import glob
import uuid
import shutil
import random
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randint, rand
import pdb

print matplotlib.get_backend()

# 分類結果の表示
def show_figure(mu, cls):
    fig = plt.figure()
    for c in range(K):
        subplot = fig.add_subplot(K,7,c*7+1)
        subplot.set_xticks([])
        subplot.set_yticks([])
        subplot.set_title('Master')
        subplot.imshow(mu[c].reshape(h,w), cmap=plt.cm.gray_r)
        i = 1
        for j in range(len(cls)):
            if cls[j] == c:
                subplot = fig.add_subplot(K,7,c*7+i+1)
                subplot.set_xticks([])
                subplot.set_yticks([])
                subplot.imshow(df.ix[j].reshape(h,w), cmap=plt.cm.gray_r)
                i += 1
                if i > 6:
                    break
    fig.show()

# ベルヌーイ分布
def bern(x, mu):
    r = 1.0
    for x_i, mu_i in zip(x, mu):
        if x_i == 1:
            r *= mu_i
        else:
            r *= (1.0 - mu_i)
    return r

# Main
if __name__ == '__main__':
    global h, w
    K = 20   # 分類するクラス数
    N = 5  # 反復回数

    input_dir = '/tmp/opencv'
    result_dir = '/tmp/opencv/result'

    # 結果格納ディレクトリの削除
    if os.path.isdir(result_dir):
        shutil.rmtree(result_dir)

    files = glob.glob(input_dir + '/*.jpg')
    files = random.sample(files, 1000)

    print 'Input Files: ' + str(len(files))

    samples = []
    # トレーニングセットの読み込み
    for f in files:
        gray = cv2.cvtColor(cv2.imread(f), cv2.COLOR_RGB2GRAY)
        h, w = gray.shape[:2]
        gray = cv2.resize(gray, (int(w / 40), int(h / 40)))
        h, w = gray.shape[:2]
        canny = cv2.Canny(gray, 50, 150)
        ret, thr = cv2.threshold(canny, 128, 1, cv2.THRESH_BINARY)
        sample = thr.reshape((h * w))
        samples.append(sample.copy())
    data_num = len(samples)

    # 初期パラメータの設定
    mix = [1.0/K] * K
    mu = (rand(h*w*K)*0.5+0.25).reshape(K, h*w)
    for k in range(K):
        mu[k] /= mu[k].sum()

    # N回のIterationを実施
    for iter_num in range(N):
        print "iter_num %d" % iter_num

        # E phase
        resp = DataFrame()
        for line in samples:
            tmp = []
            for k in range(K):
                a = mix[k] * bern(line, mu[k])
                if a == 0:
                    tmp.append(0.0)
                else:
                    s = 0.0
                    for kk in range(K):
                        s += mix[kk] * bern(line, mu[kk])
                    tmp.append(a/s)
            resp = resp.append([tmp], ignore_index=True)

        # M phase
        mu = np.zeros((K, h*w))
        for k in range(K):
            nk = resp[k].sum()
            mix[k] = nk/data_num
            index = 0
            for line in samples:
                mu[k] += line * resp[k][index]
                index += 1
            mu[k] /= nk

    # トレーニングセットの文字を分類
    cls = []
    for index, line in resp.iterrows():
        cls.append(np.argmax(line[0:]))

    if not os.path.isdir(result_dir):
        os.mkdir(result_dir)

    index = 0
    for cl in cls:
        file_path = files[index]
        class_num = str(cl)
        if not os.path.isdir(os.path.join(result_dir, class_num)):
            os.mkdir(os.path.join(result_dir, class_num))
        dst_path = os.path.join(result_dir, class_num, os.path.basename(file_path))
        shutil.copyfile(file_path, dst_path)
        index += 1

    # 分類結果の表示
    # show_figure(mu, cls)
