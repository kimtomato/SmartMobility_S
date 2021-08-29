#!/usr/bin/python3

import sys
import cv2 as cv

n = len(sys.argv)
if n < 2 :
	sys.exit(f"usage : { sys.argv[0] } file")

img_file = sys.argv[1]
img = cv.imread(img_file)
if img is None:
	sys.exit(f"{img_file} is not an image file ")

cv.imshow(img_file, img)
print("press any key to exit")
cv.waitKey(0)
	
