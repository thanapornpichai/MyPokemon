import cv2 as cv
import numpy as np

image1 = cv.imread("teddiursa.png")
image2 = cv.imread("pikachu.png")

gray_image1 = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)
gray_image2 = cv.cvtColor(image2, cv.COLOR_BGR2GRAY)

ret1, binary_image1 = cv.threshold(gray_image1, 127, 255, cv.THRESH_BINARY)
ret2, binary_image2 = cv.threshold(gray_image2, 127, 255, cv.THRESH_BINARY)

height, width = gray_image1.shape

canvas = np.zeros((height * 2, width * 2), dtype=np.uint8)

canvas[0:height, 0:width] = gray_image1
canvas[0:height, width:width * 2] = binary_image1
canvas[height:height * 2, 0:width] = gray_image2
canvas[height:height * 2, width:width * 2] = binary_image2

center_coordinates = (width // 2, height // 2)
radius = min(width, height) // 4
color = 255
thickness = 2
canvas = cv.circle(canvas, center_coordinates, radius, color, thickness)

cv.imshow("Pokemon", canvas)

cv.waitKey(0)
cv.destroyAllWindows()
