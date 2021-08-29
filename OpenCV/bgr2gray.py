#!/usr/bin/python3

import sys
import cv2 as cv

n = len(sys.argv)
if n<3 :
	sys.exit(f"usage:{sys.argv[0]} input file output file")

img_file = sys.argv[1]
img = cv.imread(img_file)
if img is None:
	sys.exit(f"{img_file} is not an image file!")
bw = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imwrite(sys.argv[2], bw)
