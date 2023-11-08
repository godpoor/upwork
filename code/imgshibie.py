import pyautogui
from PIL import Image
import pytesseract

# 定义屏幕区域的坐标
x1, y1, x2, y2 = (100, 100, 300, 300)  # 你可以根据需要修改坐标

# 使用pyautogui截取指定屏幕区域的图像
screenshot = pyautogui.screenshot(region=(312, 14, 95, 32))

# 将截图保存为图像文件
screenshot.save("screenshot.png")

# 使用Pytesseract识别文字
text = pytesseract.image_to_string(Image.open("screenshot.png"))

# 打印识别的文本
print(text)
