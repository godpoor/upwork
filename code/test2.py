#修改备注为指定备注名称

import pyautogui
import time
a = [1,1]
b = [300,518]
# c = [670,29]

i = 1
# pyautogui.click(a[0], a[1])
# pyautogui.click(b[0], b[1])
# pyautogui.click(c[0], c[1])
# 在指定区域中搜索图像的位置
image_location = pyautogui.locateOnScreen('newmessage.png', region=(a[0], a[1], b[0] - a[0], b[1] - a[1]))

if image_location is not None:
    x, y, width, height = image_location
    print(f"图像位置：x={x}, y={y}, 宽度={width}, 高度={height}")
else:
    print("未找到图像")
