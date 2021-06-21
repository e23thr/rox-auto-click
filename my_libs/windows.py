import os
import pyautogui
from win32api import GetSystemMetrics

print("Program is running on Windows")


def get_screen_resolution():
    return {"width": GetSystemMetrics(0), "height": GetSystemMetrics(1)}


def locate_btn_start_fishing(on_retina:bool=False):
    return pyautogui.locateOnScreen(os.path.join(os.getcwd(), "images","start-fishing.png"),confidence=0.5)

def click_btn_setting(on_retina:bool=False):
    position = locate_btn_start_fishing()
    if position is None:
      print('ERROR')
      return
    x, y = pyautogui.center(position)
    return pyautogui.click(x=x,y=y)