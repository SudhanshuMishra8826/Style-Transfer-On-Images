import argparse
import imutils
import time
import cv2

style="starry_night.t7"
net = cv2.dnn.readNetFromTorch(style)
image = cv2.imread('night.jpg')
image = imutils.resize(image, width=600)
(h, w) = image.shape[:2]

blob = cv2.dnn.blobFromImage(image, 1.0, (w, h),
	(103.939, 116.779, 123.680), swapRB=False, crop=False)
net.setInput(blob)

output = net.forward()

output = output.reshape((3, output.shape[2], output.shape[3]))
output[0] += 103.939
output[1] += 116.779
output[2] += 123.680
output /= 255.0
output = output.transpose(1, 2, 0)


cv2.imshow("Input", image)
cv2.imshow("Output", output)
cv2.waitKey(0)