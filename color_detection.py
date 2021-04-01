import numpy as np 
import cv2
image = cv2.imread("yellow_shirt.jpg")
boundaries = [
	([17, 15, 100], [50, 56, 200]),  #red
	([86, 31, 4], [220, 88, 50]),    #blue
	([25, 146, 190], [62, 174, 250]), #yellow
	([103, 86, 65], [145, 133, 128]) #green
]
colors = [
	"red",
	"blue",
	"yellow",
	"green"
]
colors_count = {}
for (lower, upper) in boundaries:
	temp_tuple = (lower, upper)
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	new = output.flatten().tolist()
	count = 0
	for i in new:
		if i != 0:
			count += 1
	#print (temp_tuple)
	idx = boundaries.index(temp_tuple)
	clr = colors[idx]
	colors_count[clr] = count
	# show the images
	#cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)
print (max(colors_count, key=colors_count.get))