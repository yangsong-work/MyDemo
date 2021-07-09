import cv2 as cv
import numpy
import time
clicked=False # 鼠标点击标记
def onMouse(event,x,y,flags,param): #鼠标点击回调事件
    global clicked
    if event == cv.EVENT_LBUTTONUP:
        clicked=True
cameroCap=cv.VideoCapture("rtsp://admin:fri123456@192.168.8.106/main/av_stream") #获取摄像头设备
cv.namedWindow('MyWindow') #创建窗口名为 mywindow的窗口
cv.setMouseCallback('MyWindow',onMouse) #设置回调事件
print('正在捕捉视频,点击按钮或者鼠标停止')
success,frame=cameroCap.read() #读取
while success and cv.waitKey(1)==-1 and not clicked: #读取成功 且 没有键盘点击 且 没有鼠标点击
    cv.imshow('MyWindow',frame)
    success,frame=cameroCap.read()
time.sleep(1) #延迟一秒释放窗口和摄像头
cv.destroyAllWindows() #释放窗口
cameroCap.release() #释放摄像头
print('结束')