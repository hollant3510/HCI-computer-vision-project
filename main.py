#Thomas Holland
#CSC 355
#Homework 4
#counts the images, edits them, and prints out statistics

import numpy as np
import cv2

# Loads in the image in grayscale
img = cv2.imread('1.jpg',0)


cv2.imshow('',img)
cv2.waitKey(0)

#prints out image with dynamic thresh holding
ret,output = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('', output)
cv2.waitKey(0)


#prints out dilated image
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(output, kernel,iterations = 1)
cv2.imshow('', dilation)
cv2.waitKey(0)

#prints out eroded image
erosion = cv2.erode(dilation,kernel,iterations = 1)
cv2.imshow('', erosion)
cv2.waitKey(0)

#removes background from list after finding image centers
nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(erosion)
centroids = np.delete(centroids, 0, 0)
stats = np.delete(stats, 0, 0)



#prints number of objects and there stats.
print("Number of Objects: ", nlabels -1)
counter = 0
for x in range(len(centroids)):
    print ("object", str(counter), " has the coordinates", centroids[x] )
    print("The width is: ", stats[x, 2])
    print("The height is: ", stats[x, 3])
    print("The area is: ", stats[x, 4])
    counter = counter + 1





cv2.destroyAllWindows()