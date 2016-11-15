from PIL import Image
import sys
from graph import build_graph, segment_graph
from smooth_filter import gaussian_grid, filter_image
from random import random
from numpy import sqrt
import numpy as np
import cv2

def diff_rgb(img, x1, y1, x2, y2):
    r = (img[0][x1, y1] - img[0][x2, y2]) ** 2
    g = (img[1][x1, y1] - img[1][x2, y2]) ** 2
    b = (img[2][x1, y1] - img[2][x2, y2]) ** 2
    return sqrt(r + g + b)

def diff_grey(img, x1, y1, x2, y2):
    v = (img[x1, y1] - img[x2, y2]) ** 2
    return sqrt(v)

def threshold(size, const):
    return (const / size)

def generate_image(forest, width, height):
    random_color = lambda: (int(random()*255), int(random()*255), int(random()*255))
    colors = [random_color() for i in xrange(width*height)]

    img = Image.new('RGB', (width, height))
    im = img.load()
    for y in xrange(height):
        for x in xrange(width):
            comp = forest.find(y * width + x)
            im[x, y] = colors[comp]

    return img.transpose(Image.ROTATE_270).transpose(Image.FLIP_LEFT_RIGHT)

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print 'Invalid number of arguments passed.'
        print 'Correct usage: python main.py sigma neighborhood K min_comp_size input_file'
    else:
        neighbor = int(sys.argv[2])
        if neighbor != 4 and neighbor!= 8:
            print 'Invalid neighborhood choosed. The acceptable values are 4 or 8.'
            print 'Segmenting with 4-neighborhood...'


        tmp_img = cv2.imread(sys.argv[5])
        h, w = tmp_img.shape[:2]
        tmp_img = cv2.resize(tmp_img, (int(w / 4), int(h / 4)))
        image_file = Image.fromarray(tmp_img, "RGB")
        sigma = float(sys.argv[1])
        K = float(sys.argv[3])
        min_size = int(sys.argv[4])

        size = image_file.size
        print 'Image info: ', image_file.format, size, image_file.mode

        grid = gaussian_grid(sigma)

        if image_file.mode == 'RGB':
            image_file.load()
            r, g, b = image_file.split()

            r = filter_image(r, grid)
            g = filter_image(g, grid)
            b = filter_image(b, grid)

            smooth = (r, g, b)
            diff = diff_rgb
        else:
            smooth = filter_image(image_file, grid)
            diff = diff_grey

        graph = build_graph(smooth, size[1], size[0], diff, neighbor == 8)
        forest = segment_graph(graph, size[0]*size[1], K, min_size, threshold)

        image = generate_image(forest, size[1], size[0])

        print 'Number of components: %d' % forest.num_sets

        cv2.namedWindow('Result')
        cv2.imshow('Result', np.array(image))

        cv2.namedWindow('Canny')
        cv2.imshow('Canny', cv2.Canny(np.array(image), 100, 10))

        cv2.waitKey(0)
        cv2.destroyAllWindows()
