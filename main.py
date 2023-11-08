import requests
import re
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
from datetime import datetime, timedelta
import sys
import time
import pyautogui
import pyperclip

usrnum = 0
flag = 0
counter = 0
warn_value = 100
standard_value = 180
usrlist = [0] * 100




def sendWxMessage(target, msg, delay_time=2):
    try:
        # 最小化所有窗口
        pyautogui.hotkey('win', 'd')
        # 清空剪切板并将目标写入到剪切板
        pyperclip.copy("")
        pyperclip.copy(target)
        # 打开微信窗口
        pyautogui.hotkey("ctrl", "alt", "w")
        time.sleep(delay_time)
        # 使用快捷键ctrl+f定位到微信搜索栏
        pyautogui.hotkey("ctrl", "f")
        time.sleep(delay_time)
        # 使用快捷键ctrl+v将目标粘贴到微信搜索栏，微信将自动搜索
        pyautogui.hotkey("ctrl", "v")
        time.sleep(delay_time)
        # 按回车键打开搜索出的目标
        pyautogui.press("enter")
        time.sleep(delay_time)
        # 清空剪切板并将未点检信息写入到剪切板
        pyperclip.copy("")
        pyperclip.copy(msg)
        # 使用快捷键ctrl+v将信息粘贴到微信输入框，按回车发送消息
        pyautogui.hotkey("ctrl", "v")
        time.sleep(delay_time)
        pyautogui.press("enter")
        # log
        print("发送微信消息")
    except Exception as ex:
        print("发送微信消息出现异常: " + str(ex))
        sys.exit(0)


def newfriend():
    global usrnum
    usrnum += 1
    global usrlist
    pyautogui.click(21, 149)
    time.sleep(1)
    pyautogui.click(143, 188)
    time.sleep(1)
    pyautogui.click(588, 101)
    time.sleep(1)
    rename = pyautogui.locateOnScreen('img/rename.png', region=(1, 1, 700, 1000))
    if rename is not None:
        x, y, width, height = rename
        pyautogui.click(x + 50, y + 36)
        time.sleep(1)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(1)
        pyautogui.hotkey("Del")
        # 清空剪切板并将未点检信息写入到剪切板
        pyperclip.copy("")
        pyperclip.copy("SSRF" + str(usrnum).zfill(3))
        # 使用快捷键ctrl+v将信息粘贴到微信输入框，按回车发送消息
        pyautogui.hotkey("ctrl", "v")
        pyautogui.click(300, 750)
        time.sleep(1)
        pyautogui.click(25, 105)
        time.sleep(1)
        pyautogui.click(200, 450)


def newmessage():
    global usrnum
    global usrlist
    pyautogui.click(20, 105)
    pyautogui.click(20, 105)
    time.sleep(1)
    pyautogui.click(160, 100)
    # 直接点击某个位置，然后循环检测用户输入信息是什么，然后回复
    xinxitixing = pyautogui.locateOnScreen('img/xinxitixing.png', region=(300, 1, 400, 380))
    dianhuatixing = pyautogui.locateOnScreen('img/dianhuatixing.png', region=(300, 1, 400, 380))
    if xinxitixing is not None:
        pyautogui.click(417, 436)
        time.sleep(1)
        pyperclip.copy("好的")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        time.sleep(1)
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
        last_four_characters = usrname[-3:]
        usrnum = int(last_four_characters)
        usrlist[usrnum] = 1
    if dianhuatixing is not None:
        pyautogui.click(417, 436)
        time.sleep(1)
        pyperclip.copy("好的")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        time.sleep(1)
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
        last_four_characters = usrname[-3:]
        usrnum = int(last_four_characters)
        usrlist[usrnum] = 2
    time.sleep(1)
    pyautogui.click(160, 100)
    time.sleep(1)
    # 模拟鼠标右键点击
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.click(200, 250)
    time.sleep(1)
    pyautogui.click(295, 310)


def clear_usr():
    global usrlist
    global usrnum
    for i in range (1,usrnum + 1):
        usrlist[i] = 0
        sendWxMessage("SSRF" + str(i).zfill(3), "请重新添加好友进行订阅，谢谢！", 2)
        # ！！！重新匹配
        pyautogui.click(680, 36)
        time.sleep(1)
        pyautogui.click(740, 50)
        time.sleep(1)
        pyautogui.click(976, 81)
        time.sleep(1)
        pyautogui.click(1055, 238)
        time.sleep(1)
        pyautogui.click(820, 280)
        time.sleep(1)
    usrnum = 0
def upwork(value):
    global flag
    global usrnum
    global usrlist
    if value > standard_value and flag == 1:  # 已经来光，提醒用户
        while usrnum >= 0:
            if usrlist[usrnum] == 1:
                sendWxMessage("SSRF" + str(usrnum).zfill(3), "已来光", 2)
                time.sleep(3)
                usrnum = usrnum - 1
            elif usrlist[usrnum] == 2:
                sendWxMessage("SSRF" + str(usrnum).zfill(3), "已来光", 2)
                pyautogui.click(630, 396)
                time.sleep(3)
                usrnum = usrnum - 1
                while True:
                    jujue = pyautogui.locateOnScreen('img/jujue.png', region=(830, 500, 100, 100))
                    jujue_fuzhu = pyautogui.locateOnScreen('img/jujue_fuzhu.png', region=(700, 400, 400, 300))
                    if jujue is None and jujue_fuzhu is None:
                        break
            else:
                usrnum = usrnum - 1
            time.sleep(1)
            pyautogui.click(160, 100)
            time.sleep(1)
            # 模拟鼠标右键点击
            pyautogui.click(button='right')
            time.sleep(1)
            pyautogui.click(200, 250)
            time.sleep(1)
            pyautogui.click(295, 310)
        flag = 0



# 忽略不安全请求的警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
inurl = "https://status.ssrf.ac.cn/ssrf/beam/"
now = datetime.now()
next_day = now + timedelta(days=1)
target_time = next_day.replace(hour=12, minute=0, second=0, microsecond=0)

# 循环检测
while True:
    new_message = pyautogui.locateOnScreen('img/newmessage.png', region=(1, 1, 55, 200))
    new_friend = pyautogui.locateOnScreen('img/newfriend.png', region=(1, 1, 55, 200))
    # 检测时间
    current_time = datetime.now()
    if current_time >= target_time:
        # 在第二天的12点执行操作
        clear_usr()
        # 更新目标时间为下一天的12点
        next_day += timedelta(days=1)
        target_time = next_day.replace(hour=12, minute=0, second=0, microsecond=0)
        time.sleep(1)
    req = requests.get(url=inurl, verify=False)
    req.encoding = "utf-8"
    html = req.text
    soup = BeautifulSoup(html, features="html.parser")
    company_items = soup.find_all("span", class_="STYLE3")
    if new_friend is not None:
        newfriend()
    if new_message is not None:
        newmessage()
    for company_item in company_items:
        # 找到下一个兄弟节点的文本内容
        next_th = company_item.find_next("th")
        if next_th:
            value_text = next_th.text.strip()
            # 使用正则表达式提取数字部分
            match = re.search(r'(\d+\.\d+)', value_text)
            if match:
                value = float(match.group(1))
                if value > standard_value:
                    upwork(value)
                    print(f"数值: {value}，大于180.00，等待10s后再次检测")
                    time.sleep(10)
                elif value < warn_value:
                    print(f"数值: {value}，小于100，等待2s后再次检测")
                    flag = 1
                    time.sleep(10)
                else:
                    print(f"数值: {value}，等待10s后再次检测")
                    time.sleep(10)
