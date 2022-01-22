import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

image = cv2.imread('../images/wall-of-faces.jpg', cv2.IMREAD_COLOR )
template = cv2.imread('../images/template-face.jpg', cv2.IMREAD_COLOR)

h, w = template.shape[:2]
method = cv2.TM_CCOEFF_NORMED

threshold = 0.86

start_time = time.time()


res = cv2.matchTemplate(image, template, method)
# Fake out max_val for first run through loop
max_val = 1
while max_val > threshold:
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
  # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
  if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
  else:
    top_left = max_loc


  if max_val > threshold:
    res[top_left[1]-h//2:top_left[1]+h//2+1, top_left[0]-w//2:top_left[0]+w//2+1] = 0   
    image = cv2.rectangle(image,(top_left[0],top_left[1]), (top_left[0]+w+1, top_left[1]+h+1), (0,255,0) )

# plt.figure(figsize=(8,8))
# plt.subplot(211)
# plt.imshow(res,cmap = 'gray')
# plt.title('Matching Result')
# plt.xticks([])
# plt.yticks([])
# plt.subplot(212)
# plt.imshow(image,cmap = 'gray')
# plt.title('Detected Point')
# plt.xticks([])
# plt.yticks([])
# plt.suptitle('Template matching with correlation coefficient')
# plt.show()
cv2.imwrite('../images/template2.jpg', image)