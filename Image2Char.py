#PIL   OpenCV  处理图像
import random

from pip._vendor.distlib.compat import raw_input
import numpy as np
from PIL import Image
from pylab import *
import tensorflow as tf
im = array(Image.open('empire.png'))
convolve(im,1)
imshow(im)
# 添加标题信息
title('Plotting: "empire.png"')

# 隐藏坐标轴
# axis('off')

# 显示到屏幕窗口
show()
def convole(image,weight):
    height,width = image.shape
    h, w = weight.shape
    height_new = height - h + 1
    width_new = width - w + 1
    image_new = np.zeros((height_new, width_new),dtype=np.float)
    for i in range(height_new):
        for j in range(width_new):
            image_new[i,j] = np.sum(image[i:i+h, j:j+w] * weight)
        image_new = image_new.clip(0,255)
        image_new = np.rint(image_new).astype('uint8')
        return image_new