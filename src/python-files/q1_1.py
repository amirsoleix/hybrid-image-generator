# Importing necessary libraries and dependencies
import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter

image = cv2.imread('../images/res01-original.jpg') # Reads original image file

###-------------------------------###
### MEAN FILTER FOR COLORED IMAGE ###
###-------------------------------###

# In RGB information concerning color and luminance can not be separated. HSV is used to separate image luminance from color information and hence is required.
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# The figure size is relatively large to better show the effect of the filter.
figure_size = 15
mean_image = cv2.blur(image,(figure_size, figure_size))

# plt.figure(figsize=(12,7))
# plt.subplot(121)
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_HSV2RGB))
# plt.title('Original (Self portrait with bandaged ear)')
# plt.xticks([])
# plt.yticks([])
# plt.subplot(122)
# plt.imshow(cv2.cvtColor(mean_image, cv2.COLOR_HSV2RGB))
# plt.title('Mean filter (Artifacts appear and detail is lost)')
# plt.xticks([])
# plt.yticks([])
# plt.show()
output_image = cv2.cvtColor(mean_image, cv2.COLOR_HSV2BGR)
cv2.imwrite('../images/res01.jpeg', output_image)

###----------------------------------###
### MEAN FILTER FOR GRAYSCALED IMAGE ###
###----------------------------------###

grayScale_image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
grayScale_image = cv2.cvtColor(grayScale_image, cv2.COLOR_BGR2GRAY)

# The figure size is chosen to better illustrate the effects of the filter
figure_size = 15
mean_grayScale = cv2.blur(grayScale_image,(figure_size, figure_size))

# plt.figure(figsize=(12,7))
# plt.subplot(121)
# plt.imshow(grayScale_image, cmap='gray'),plt.title('Original (Gray scaled image of the painting)')
# plt.xticks([])
# plt.yticks([])
# plt.subplot(122)
# plt.imshow(mean_grayScale, cmap='gray')
# plt.title('Mean filter (Removes noises and details, No artifacts)')
# plt.xticks([])
# plt.yticks([])
# plt.show()
output_image = cv2.cvtColor(mean_grayScale, cv2.COLOR_GRAY2BGR)
cv2.imwrite('../images/res01-grayscale.jpeg', output_image)

###-----------------------------------###
### GAUSSIAN FILTER FOR COLORED IMAGE ###
###-----------------------------------###

gaussian_image = cv2.GaussianBlur(image, (figure_size, figure_size),0)

# plt.figure(figsize=(12,7))
# plt.subplot(121)
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_HSV2RGB))
# plt.title('Original (Self portrait with bandaged ear)')
# plt.xticks([])
# plt.yticks([])
# plt.subplot(122)
# plt.imshow(cv2.cvtColor(gaussian_image, cv2.COLOR_HSV2RGB))
# plt.title('Gaussian Filter (Retains detail and produces few artifacts)')
# plt.xticks([])
# plt.yticks([])
# plt.show()
output_image = cv2.cvtColor(gaussian_image, cv2.COLOR_HSV2BGR)
cv2.imwrite('../images/res02.jpeg', output_image)

###--------------------------------------###
### GAUSSIAN FILTER FOR GRAYSCALED IMAGE ###
###--------------------------------------###

gaussian_grayscale = cv2.GaussianBlur(grayScale_image, (figure_size, figure_size),0)

# plt.figure(figsize=(12,7))
# plt.subplot(121)
# plt.imshow(grayScale_image, cmap='gray')
# plt.title('Original (Gray scaled image of the painting)')
# plt.xticks([])
# plt.yticks([])
# plt.subplot(122)
# plt.imshow(gaussian_grayscale, cmap='gray')
# plt.title('Gaussian Filter (Retains detail and does not produce artifact)')
# plt.xticks([])
# plt.yticks([])
# plt.show()
output_image = cv2.cvtColor(gaussian_grayscale, cv2.COLOR_GRAY2BGR)
cv2.imwrite('../images/res02-grayscale.jpeg', output_image)