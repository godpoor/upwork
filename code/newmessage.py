import time

import  pyautogui
# 引入pyperclip模块以操作剪切板
import pyperclip
tixing = pyautogui.locateOnScreen('img/xinxitixing.png', region=(300,1,400,380))
if tixing is not None:
    x,y,w,h = tixing
    pyautogui.click(417, 436)
    time.sleep(1)
    # pyperclip.copy("好的")
    # pyautogui.hotkey("ctrl", "v")
    # pyautogui.press("enter")
    pyautogui.click(350, 30)
    time.sleep(1)
    pyautogui.click(740, 50)
    time.sleep(1)
    pyautogui.click(852, 90)
    pyautogui.click(852, 90)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "c")
    # 将剪贴板中的内容粘贴到变量a中
    usrname = pyperclip.paste()
    # 使用切片操作提取后四个字符
    last_four_characters = usrname[-4:]

    # 将提取的字符转换为整数
    try:
        last_four_as_int = int(last_four_characters)
        print("后四个字符作为整数：", last_four_as_int)
    except ValueError:
        print("无法转换为整数：", last_four_characters)
    # 打印变量a的值
    print(usrname)
    # time.sleep(1)
    # pyautogui.hotkey("ctrl", "v")
    # print(x,y)