import cv2

landscape = cv2.imread('Homework\Images\Landscape.png')
cv2.imshow('Original Image', landscape)
cv2.waitKey(0)

greyscaledLandscape = cv2.cvtColor(landscape, cv2.COLOR_BGR2GRAY)
cv2.imshow('Greyscaled Image', greyscaledLandscape)
cv2.waitKey(0)

HSVLandscape = cv2.cvtColor(landscape, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', HSVLandscape)
cv2.waitKey(0)

ironman1 = cv2.imread('Homework\Images\Iron Man.png')
ironman2 = cv2.imread('Homework\Images\Iron Man 2.png')

imageAdded = cv2.addWeighted(ironman1, 0.5, ironman2, 0.5, 0)

cv2.imshow('Image Addition', imageAdded)
cv2.waitKey(0)

cv2.imwrite('Homework\Image Conversion and Display Using OpenCV\Greyscaled Landscape.png', greyscaledLandscape)
cv2.imwrite('Homework\Image Conversion and Display Using OpenCV\HSV Landscape.png', HSVLandscape)

cv2.destroyAllWindows()