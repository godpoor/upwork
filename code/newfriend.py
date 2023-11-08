import time
import  pyautogui
# 引入pyperclip模块以操作剪切板
import pyperclip
usrlist = []
usrnum =1
rename = pyautogui.locateOnScreen('img/rename.png', region=(1,1,700,1000))
accept = pyautogui.locateOnScreen('img/accept.png', region=(1,1,700,1000))
if rename is not None:
    x, y, width, height = rename
    pyautogui.click(x+50, y+36)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(1)
    pyautogui.hotkey("Del")
    # 清空剪切板并将未点检信息写入到剪切板
    pyperclip.copy("")
    pyperclip.copy("SSRF"+str(usrnum).zfill(3))
    usrlist.append(0)
    usrnum = usrnum + 1
    # 使用快捷键ctrl+v将信息粘贴到微信输入框，按回车发送消息
    pyautogui.hotkey("ctrl", "v")
    x, y, width, height = accept
    print(usrlist[0])
