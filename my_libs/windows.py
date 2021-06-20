import pyautogui
from win32api import GetSystemMetrics

print("Program is running on Windows")


def is_retina():
    return False


def get_screen_resolution():
    return {"width": GetSystemMetrics(0), "height": GetSystemMetrics(1)}
