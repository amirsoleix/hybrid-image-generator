import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/line.jpg')
img2 = img.copy()
figure_size = 5
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(gray,(figure_size, figure_size),0)
edges = cv2.Canny(img,50,150,apertureSize = 3)
minLineLength = 5
maxLineGap = 0
lines = cv2.HoughLinesP(edges,1,np.pi/180,10,minLineLength = minLineLength,maxLineGap = maxLineGap)
for i in range (0,len(lines)):
  for x1,y1,x2,y2 in lines[i]:
    cv2.line(img2,(x1,y1),(x2,y2),(0,255,0),2)

plt.figure(figsize=(8,5))
plt.subplot(111)
plt.imshow(img2,cmap = 'gray')
plt.title('Detected Lines')
plt.xticks([])
plt.yticks([])
plt.show()

cv2.imwrite('../images/res3_5.jpg',img2)