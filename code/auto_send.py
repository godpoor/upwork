# -*- coding: UTF-8 -*-
import sys
import time
# 引入pyautogui模块以操作快捷键
import pyautogui
# 引入pyperclip模块以操作剪切板
import pyperclip

#电机
# a = [100,100]

def sendWxMessage(target, msg, delay_time=2):
    """
    实现原理：1、通过打开微信的快捷键ctrl+alt+w,打开微信窗口
            2、通过搜索快捷键ctrl+f,打开搜索窗口
            3、通过ctrl+v快捷键实现输入功能
            4、通过ctrl+enter快捷键实现搜索or发送功能
    :param target: 发送目标
    :param msg: 需要发送的消息
    :param delay_time: 延迟时间 默认2秒
    :return:无返回值
    """
    try:
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


if __name__ == '__main__':
    sendWxMessage("文件传输助手", "开启检测，检测时间为24H", 2)
    # sendWxMessage("1", "测试", 2)
    print("下一步")