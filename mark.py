import cv2
import numpy as np
import math
import pandas as pd
import csv
count = 0

def mouse_handler(event, x0, y0, flags, data):
    if event == cv2.EVENT_LBUTTONDOWN:
        point_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        global count
        name = point_name[count]

        #平移座標原點
        #以右下角為原點 縱軸向上為+y 橫軸向右為+x
        x = x0 - 1920
        y = -y0 + 1080

        #轉動角度以+Y軸為0，沿逆時鐘方向增加
        degree = round(math.degrees(math.atan(y/x))+ 90,2)
        text = str(degree)
        # 標記點位置
        cv2.circle(data['img'], (x0,y0), 3, (0,255,255), 5, 16) 
        cv2.putText(data['img'],name + ' ('+str(x)+','+str(y)+') theta = '+ text, (x0 + 5,y0 - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (100,255,255), 2, cv2.LINE_AA)
        # 改變顯示 window 的內容
        cv2.imshow("Image", data['img'])

        # 顯示 點名稱、點座標(x,y)、角度 並儲存到 list中
        print("get points {}: (x, y) = ({}, {}) θ = {}".format(name,x,y,degree))
        data['point_name'].append(name)
        data['coordinate_x'].append(x)
        data['coordinate_y'].append(y)
        data['theta'].append(degree)
        count += 1

        with open('point.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = ['value', 'point_name', 'coordinate_x', 'coordinate_y', 'theta'])
            writer.writeheader()
            writer.writerow({'value': count - 1, 'point_name': name, 'coordinate_x': x, 'coordinate_y': y, 'theta':degree})
    cv2.imwrite("output.png", data['img'])



def get_points(im):
    # 建立 data dict, img:存放圖片, point:存放點名稱,coordinate:存放點座標 theta:存放角度
    data = {}
    data['img'] = im.copy()
    data['point_name'] = []
    data['coordinate_x'] =[]
    data['coordinate_y'] = []
    data['theta'] = []
    
    # 建立一個 window
    cv2.namedWindow("Image", 0)
    
    # 改變 window 成為適當圖片大小
    #h, w, dim = im.shape
    #print("Img height, width: ({}, {})".format(h, w))
    #cv2.resizeWindow("Image", w, h)
        
    # 顯示圖片在 window 中
    cv2.imshow('Image',im)
    
    # 利用滑鼠回傳值，資料皆保存於 data dict中
    cv2.setMouseCallback("Image", mouse_handler, data)
    
    # 等待按下任意鍵，藉由 OpenCV 內建函數釋放資源
    cv2.waitKey()
    cv2.destroyAllWindows()
    # 回傳點 list
    return data

#Read the image
img_dst = cv2.imread("t0001.png")

data = get_points(img_dst)

df = pd.DataFrame(data, columns = ['point_name', 'coordinate_x', 'coordinate_y', 'theta'])
print(df)


    #writer = csv.writer(csvfile, delimiter=' ')
    #writer.writerow(['point_name', 'coordinate_x', 'coordinate_y', 'theta'])
    #for p in data:
        #writer.writerow(p)
    #writer = csv.DictWriter(csvfile, fieldnames = ['point_name', 'coordinate_x', 'coordinate_y', 'theta'])
    #writer.writeheader()
    #for p in data:
    #    writer.writerow(p)