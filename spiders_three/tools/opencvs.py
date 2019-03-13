# _*_ coding:utf-8 _*_
import numpy as np
import cv2
import matplotlib as mpl
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt

img = cv2.imread('touxiang.jpg',0)
img2 = cv2.imread('head.png',0)
img3 = cv2.imread('head.png',0)
#plt.imshow(img,cmap='gray',interploation='bicubic')
fig = plt.figure()

ax = fig.add_subplot(221)
ax.imshow(img)

ax = fig.add_subplot(222)
cmap=mpl.cm.hot
ax.imshow(img,cmap=cmap)

ax = fig.add_subplot(223)
cmap=mpl.cm.cool
ax.imshow(img2,cmap=cmap)

ax = fig.add_subplot(224)
cmap=mpl.cm.cool
ax.imshow(img2,cmap=cmap)

#隐藏刻度值
plt.xticks([]),plt.yticks([]) #to hide tick values on x and y axis
plt.show()
