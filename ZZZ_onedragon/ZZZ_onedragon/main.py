import ctypes, sys
import time
from pynput import keyboard,mouse
from pynput.mouse import Button
import pyautogui
import ctypes
import time
import subprocess
import logging
from ast import Try
import tkinter as tk


# 加载用户32库
user32 = ctypes.windll.user32

def bring_window_to_front(hwnd):
    # 检查窗口是否最小化，如果是则恢复窗口
    if user32.IsIconic(hwnd):
        user32.ShowWindow(hwnd, 9)  # 9 是 SW_RESTORE 的值，用于恢复窗口

    # 将窗口放到最前面
    user32.SetForegroundWindow(hwnd)

# 示例：将句柄为 hwnd 的窗口放到前台


#获取屏幕分辨率
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

logger=logging.getLogger(__name__)
logging.basicConfig(filename='myapp. log',level=logging. INFO)
# 定义必要的结构体和常量
PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def press_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
def click(x=960,y=540):
    Mouse = mouse.Controller()
    Keyboard = keyboard.Controller()
    press_key(0x38)
    time.sleep(0.1)
    Mouse.position=(x,y)
    Mouse.click(Button.left,1)
    release_key(0x38)
def keybdclick(hexKeyCode,keeptime:float=0.2):
    press_key(hexKeyCode)
    time.sleep(keeptime)
    release_key(hexKeyCode)
    if hexKeyCode == F:
        time.sleep(1)

def locateclick(png_road:str):
    while True:
        try:
            locate = pyautogui.locateCenterOnScreen(image=png_road,confidence=0.8)
            if locate is not None:
                x, y = locate
                click(x, y)
                click(1107/1920*screen_width,625/1080*screen_height)
                time.sleep(1)
                break
        except Exception as e:
            time.sleep(0.5)
            logging.info("wait_loading or cont find")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def map_find(mainplace:str,viceplace:str):
    keybdclick(M)
    time.sleep(2)
    try:
        pyautogui.locateCenterOnScreen(image='map_lock.png',confidence=0.8)
    except:
        map_find(mainplace,viceplace)
    while True:
        try:
            pyautogui.locateCenterOnScreen(image=mainplace,confidence=0.8)
            locateclick(viceplace)
            time.sleep(0.5)
            c=1126/1920*screen_width
            d=647/1080*screen_height
            click(c,d)
            break
        except:
            a=1388*screen_width/1920
            b=444*screen_height/1080
            click(a,b)
            time.sleep(1)
def locate_until(pngtolocate:str):
    while True:
        try:
            pyautogui.locateCenterOnScreen(image=pngtolocate,confidence=0.7)
            break
        except Exception:
            time.sleep(1)
# 录像店营业
def random(person_png:str='18_random.png'):
#代理人默认为安比
    map_find('random.png', 'staff.png')
    locate_until('q.png')
    keybdclick(S, 2)
    keybdclick(A, 0.22)
    keybdclick(S, 0.1)
    keybdclick(D, 0.13)
    keybdclick(F)
    time.sleep(5)
    try:
        pyautogui.locateCenterOnScreen('cancel.png')
        locateclick('cancel.png')
    except:
        time.sleep(0.5)
    locateclick('random_choose.png')
    locateclick(person_png)
    locateclick('enter.png')
    locateclick('film.png')
    time.sleep(2)
    try:
        pyautogui.locateCenterOnScreen('film_up.png')
        locateclick('film_up.png')
    except:
        click(623 * 1920 / screen_width, 261 * 1080 / screen_height)
        locateclick('Up_random.png')
        click(846 * 1920 / screen_width, 261 * 1080 / screen_height)
        locateclick('Up_random.png')
        click(1053 * 1920 / screen_width, 261 * 1080 / screen_height)
        locateclick('Up_random.png')
        locateclick('exit.png')
    locateclick('over_film.png')
    locateclick('queren.png')
    locateclick('queren.png')
    locateclick('exit.png')
def Dog():
    map_find('street.png','dog.png')
    locate_until('q.png')
    keybdclick(W,1)
    keybdclick(F)
    locateclick('guaguaka.png')
    Mouse=mouse.Controller()
    Mouse.position=(805/1920*screen_width,540/1080*screen_height)
    Mouse.press(Button.left)
    while Mouse.position[0]<=1088/1920*screen_width:
        Mouse.move(10,0)
        time.sleep(0.1)
    Mouse.position=(805/1920*screen_width,570/1080*screen_height)
    while Mouse.position[0]<=1088/1920*screen_width:
        Mouse.move(10,0)
        time.sleep(0.1)
    Mouse.position=(805/1920*screen_width,600/1080*screen_height)
    while Mouse.position[0]<=1088/1920*screen_width:
        Mouse.move(10,0)
        time.sleep(0.1)
    Mouse.release(Button.left)
    locateclick('queren.png')
    locateclick('exit.png')
    locateclick('exit.png')
def Noodle():
    ##默认白碗草本汤面
    map_find('street.png','Noodle_shop.png')
    locate_until('q.png')
    keybdclick(W, 1)
    keybdclick(F)
    locateclick('Noodletoeat.png')
    locateclick('Deal_Noodle.png')
    locateclick('queren.png')
    time.sleep(5)
    try:
        pyautogui.locateCenterOnScreen('skip.png')
        locateclick('skip.png')
    except:
        time.sleep(10)
    locateclick('queren.png')
def Coffee():
    map_find('street.png','coffee.png')
    locate_until('q.png')
    keybdclick(F)
    time.sleep(3)
    locateclick('Coffee_pure.png')
    locateclick('Deal.png')
    time.sleep(5)
    locateclick('skip.png')
    locateclick('queren.png')
    locateclick('queren.png')
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
INPUT_MOUSE = 0
A=0x1E
D=0x20
F=0x21
M=0x32
S=0x1F
W=0x11
F2=0x3C
Left_Shift=0x2A
Left_Alt=0x38
Backspace=0x0E
if __name__=='__main__':

    if is_admin():
        logging.info("start")
        try:
            file_to_open="E:/miHoYo Launcher/launcher.exe"
            subprocess.Popen(file_to_open)
            time.sleep(5)
            # 启动!
            locateclick('link_startle.png')
            time.sleep(10)
            # 获取句柄并最大化
            hwnd = user32.FindWindowW(None, "绝区零")
            if hwnd:
                bring_window_to_front(hwnd)
            else:
                logging.info('cont find window')
            time.sleep(30)
            #点击进入
            while True:
                try:
                    pyautogui.locateCenterOnScreen('open_lock.png')
                    locateclick('open.png')
                    break
                except:
                    time.sleep(0.2)
            #等待加载

            #月卡 locateclick('month_card.png')'''
            time.sleep(10)
            #录像店　以11号为例
            random()
            #刮刮乐
            Dog()
            Noodle()
            Coffee()




        except Exception:
            logging.error("wrong")

    else:
        #以管理员权限重新运行程序
        ctypes.windll.shell32.ShellExecuteW(None,"runas", sys.executable,'main.py', None, 1)
        ##logging.info("try to use root to run")




