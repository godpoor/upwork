import time

# 获取当前时间戳
start_time = time.time()

# 定义计数器的初始值
counter = 0

# 定义目标时间间隔（24小时）
target_interval = 10  # 24小时 = 24 * 60分钟 * 60秒

while True:
    # 获取当前时间戳
    current_time = time.time()

    # 计算经过的时间
    elapsed_time = current_time - start_time

    # 如果经过的时间大于等于目标时间间隔，输出"你好"，并重新开始计数
    if elapsed_time >= target_interval:
        print("你好")

        # 重置开始时间
        start_time = time.time()

        # 重置计数器
        counter = 0

    # 输出计数器的值
    print(f"计数器: {counter}")

    # 延迟一秒
    time.sleep(1)

    # 增加计数器
    counter += 1
