import cv2
from imutils import contours import numpy as np
import argparse
import imutils
import matplotlib.pyplot as plt
img = cv2.imread("/Users/zuhaibakhtar/Desktop/cpt.png",0) img = cv2.bilateralFilter(img,2,100,100)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(10,10)) img = clahe.apply(img)
"""
cv2.namedWindow("main", cv2.WINDOW_NORMAL)
cv2.imshow('main',img)
"""
gradX = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=-1)
gradX = np.absolute(gradX)
(minVal, maxVal) = (np.min(gradX), np.max(gradX))
gradX = (255 * ((gradX - minVal) / (maxVal - minVal)))
gradX = gradX.astype("uint8")
"""
cv2.namedWindow("gradX", cv2.WINDOW_NORMAL)
cv2.imshow('gradX',gradX)
"""
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKernel)
thresh = cv2.threshold(gradX, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel) """
cv2.namedWindow("thresh", cv2.WINDOW_NORMAL) cv2.imshow('thresh',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE) cnts = imutils.grab_contours(cnts)
locs = []
for (i, c) in enumerate(cnts):
(x, y, w, h) = cv2.boundingRect(c) ar = w / float(h)
if ar > 6:
#cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1) print(x,y,ar,x*y)
print(locs)
i=locs[0][0]-3 j=locs[0][1]
locs.append((x, y, w, h))
img1 = cv2.imread("/Users/zuhaibakhtar/Desktop/cpt.png") ar=[]
cntr = 0
while i<locs[0][0]+locs[0][2]:
j=locs[0][1]
count=0
while j<locs[0][1]+locs[0][3]-2:
if img[j][i]<100: count+=1
j+=1 ar.append(count)
if ar[len(ar)-1] > 0 and ar[len(ar)-2] == 0: cntr+=1
if cntr == 8: break
j=locs[0][1]
while j<locs[0][1]+locs[0][3]-2:
if 0<100:
img1[j][i] = 255
j+=1 i+=1
"""
plt.plot(ar)
plt.ylabel('count')
plt.show()
cv2.namedWindow("main", cv2.WINDOW_NORMAL) cv2.imshow('main',img)
"""
cv2.namedWindow("main1", cv2.WINDOW_NORMAL) cv2.imshow('main1',img1) #cv2.imwrite("/Users/zuhaibakhtar/Desktop/output1.png",img1) cv2.waitKey(0)
cv2.destroyAllWindows()
