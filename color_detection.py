import numpy as np 
import cv2
image = cv2.imread("red_shirt.jpg")
boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
]
d = {}
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)


'''
intialize a dict before the for loop

for each output image, check how many of the pixels are not black

put the number of pixels that are not black and the color that the output was checking for (like what index it is in boundaries) in a dictionary

after the for loop choose the color with the highest number of pixels that are not black from the dictionary
'''