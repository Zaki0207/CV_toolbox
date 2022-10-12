import cv2
import numpy as np
import os

file_path = '/Users/zhaozizyu/Downloads/zy/frame-000020.depth.png'
raw_file_path = '/Users/zhaozizyu/Documents/NeRF/实验记录/tree2/office_tree/depth_raw/depth1.raw'

imgDepth_data = np.fromfile(raw_file_path, dtype=np.uint16) # original value

imgDepth_orig = cv2.imread(file_path, cv2.IMREAD_ANYDEPTH)  # BGR / depth

print(imgDepth_orig.shape, imgDepth_orig.dtype)
print('max: ', imgDepth_orig.max())
print('min: ', imgDepth_orig.min())
print('mean: ', imgDepth_orig.mean())

imgDepth = imgDepth_orig / imgDepth_orig.max() * 255
imgDepth = 255 - imgDepth
imgDepth = imgDepth.astype(np.uint8)
img_show = cv2.applyColorMap(imgDepth, cv2.COLORMAP_JET) # colormap type of depth map
img_show_gray = cv2.cvtColor(img_show, cv2.COLOR_RGB2GRAY) # gray type of depth map
cv2.imshow('imgDepth',img_show)
cv2.waitKey(0) 