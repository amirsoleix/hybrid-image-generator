# Importing necessary libraries and dependencies
import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter

# Read image files
noise = cv2.imread('../images/noise.jpg')
noise1 = cv2.imread('../images/noise1.jpg')

###-------------------------------###
### MEDIAN FILTER FOR NOISE IMAGE ###
###-------------------------------###

# In RGB information concerning color and luminance can not be separated. HSV is used to separate image luminance from color information and hence is required.
noise = cv2.cvtColor(noise, cv2.COLOR_BGR2HSV)
noise1 = cv2.cvtColor(noise1, cv2.COLOR_BGR2HSV)

figure_size = 5
median_noise = cv2.medianBlur(noise, figure_size)
plt.figure(figsize=(9,7))
plt.subplot(221)
plt.imshow(cv2.cvtColor(noise, cv2.COLOR_HSV2RGB))
plt.title('Original picture of Asian man')
plt.xticks([])
plt.yticks([])
plt.subplot(222)
plt.imshow(cv2.cvtColor(median_noise, cv2.COLOR_HSV2RGB))
plt.title('Median Filter (Size 5 for best result)')
plt.xticks([])
plt.yticks([])

###--------------------------------###
### MEDIAN FILTER FOR NOISE1 IMAGE ###
###--------------------------------###

figure_size = 3
median_noise1 = cv2.medianBlur(noise1, figure_size)
plt.subplot(223)
plt.imshow(cv2.cvtColor(noise1, cv2.COLOR_HSV2RGB))
plt.title('Original picture of tiger')
plt.xticks([])
plt.yticks([])
plt.subplot(224)
plt.imshow(cv2.cvtColor(median_noise1, cv2.COLOR_HSV2RGB))
plt.title('Median Filter (Size 3 for best result)')
plt.xticks([])
plt.yticks([])
plt.show()