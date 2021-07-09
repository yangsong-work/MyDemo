import cv2

cap = cv2.VideoCapture("rtsp://admin:fri123456@192.168.8.106/main/av_stream")
print(cap.isOpened())