from pynput import keyboard
import time

# 字典来存储每个按键的按下时间
key_press_times = {}


def on_press(key):
    # 记录按下的时间
    key_press_times[key] = time.time()


def on_release(key):
    # 计算按键持续时间
    press_time = key_press_times.get(key)
    if press_time is not None:
        duration = time.time() - press_time
        with open("random.txt", "a") as f:
            f.write(f'{key}: {duration:.4f} seconds\n')
        # 删除记录
        del key_press_times[key]

    # 如果按下 Esc 键，则停止监听
    if key == keyboard.Key.esc:
        return False
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    with keyboard.Listener(on_press=on_press, on_release=on_release, ) as listener:
        listener.join()

    # 主程序写在这里
else:
    # 以管理员权限重新运行程序
    ctypes.windll.shell32.ShellExecuteW(None,"runas", sys.executable, __file__, None, 1)


