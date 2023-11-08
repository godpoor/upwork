import time
import  pyautogui

phone = pyautogui.locateOnScreen('img/phone.png', region=(600,380,120,50))

pyautogui.click(630, 396)
time.sleep(5)
while True:
    jujue = pyautogui.locateOnScreen('img/jujue.png', region=(830, 500, 100, 100))
    jujue_fuzhu = pyautogui.locateOnScreen('img/jujue_fuzhu.png', region=(700, 400, 400, 300))
    # time.sleep(10)
    if jujue is  None and jujue_fuzhu is None:
        break
print("已结束")
# if phone is not None:
#     x,y,w,h = phone
#     print(x,y)
#     pyautogui.click(x +8, y + 8)
#     time.sleep(5)
#     while True:
#         if jujue is not None:
#             time.sleep(5)
#         break
#     print("已结束")