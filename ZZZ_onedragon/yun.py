import time
import ctypes, sys

import pyautogui

from main import map_find
from main import keybdclick
from main import locateclick,Dog

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    time.sleep(5)
    Dog()

    # 主程序写在这里
else:
    # 以管理员权限重新运行程序
    ctypes.windll.shell32.ShellExecuteW(None,"runas", sys.executable, __file__, None, 1)


