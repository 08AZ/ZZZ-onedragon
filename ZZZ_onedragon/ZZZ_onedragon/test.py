import ctypes
user32=ctypes.windll.user32
hwnd=user32.FindWindowW(None,'绝区零')
if hwnd:
    print(hwnd)