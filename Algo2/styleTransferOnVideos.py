import argparse
import imutils
import time
import cv2
from imutils.video import VideoStream


style="starry_night.t7"
net = cv2.dnn.readNetFromTorch(style)

vs = VideoStream(src=0).start()
time.sleep(2.0)

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=600)
    orig = frame.copy()
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (w, h),(103.939, 116.779, 123.680),swapRB=False, crop=False)
    net.setInput(blob)
    output = net.forward()
    output = output.reshape((3, output.shape[2], output.shape[3]))
    output[0] += 103.939
    output[1] += 116.779
    output[2] += 123.680
    output /= 255.0
    output = output.transpose(1, 2, 0)
    cv2.imshow("Input", frame)
    cv2.imshow("Output", output)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
    	break
cv2.destroyAllWindows()
vs.stop()