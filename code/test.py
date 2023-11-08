#修改备注为指定备注名称

import pyautogui
import time
a = [1,1]
b = [700,550]
# c = [670,29]

i = 1
# pyautogui.click(a[0], a[1])
# pyautogui.click(b[0], b[1])
# pyautogui.click(c[0], c[1])
# 在指定区域中搜索图像的位置
image_location = pyautogui.locateOnScreen('test.png', region=(a[0], a[1], b[0] - a[0], b[1] - a[1]))

if image_location is not None:
    x, y, width, height = image_location
    print(f"图像位置：x={x}, y={y}, 宽度={width}, 高度={height}")
    pyautogui.click(x + 12, y+5)
    time.sleep(1)
    pyautogui.click(x + 12+65, y + 5+ 19)
    # time.sleep(1)
    # pyautogui.click(x + 12 + 65 + 150, y + 5 + 19+125)
    time.sleep(1)
    pyautogui.click(x + 12 + 65 + 247, y + 5 + 19 + 135)
    time.sleep(1)
    pyautogui.click(x + 12 + 65 + 247, y + 5 + 19 + 135)
    time.sleep(1)
    pyautogui.click(x + 12 + 65 + 150, y + 5 + 19+130)
    # 模拟按下Ctrl+A
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)  # 等待一秒钟

    # 模拟按下Delete键
    pyautogui.press('delete')
    time.sleep(1)  # 等待一秒钟

    # 模拟输入'i'（可以根据需要多次使用pyautogui.write）
    pyautogui.write("SSRF" +
                    str(i))
    time.sleep(1)  # 等待一秒钟

    # 模拟按下Enter键
    pyautogui.press('enter')
else:
    print("未找到图像")
