import cv2

#選擇攝影機
#參考 https://www.ispyconnect.com/camera/d-link
cap1 = cv2.VideoCapture('rtsp://admin:451466@192.168.0.104/live/profile.0')
cap2 = cv2.VideoCapture('rtsp://admin:227182@192.168.0.106/live/profile.0')
#cap = cv2.VideoCapture(1)

while(True):
  # 從攝影機擷取一張影像
  ret1, frame1 = cap1.read()
  ret2, frame2 = cap2.read()
  # 顯示圖片(1080, 1920, 3)
  cv2.imshow('frame1', frame1)
  cv2.imshow('frame2', frame2)

  # 若按下 q 鍵則離開迴圈
  if cv2.waitKey(1) & 0xFF == ord('q'):
    #cv2.imwrite("picture.png", frame1)
    break

# 釋放攝影機
cap1.release()
cap2.release()
# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()