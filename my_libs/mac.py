from PIL.ImageOps import grayscale
import pyautogui
import subprocess
from AppKit import NSScreen
import os

print("Program is running on Mac")


def is_retina():
    return subprocess.call("system_profiler SPDisplaysDataType | grep -i 'retina'", shell=True) == 0


def get_screen_resolution():
    return {"width": NSScreen.mainScreen().frame().size.width, "height": NSScreen.mainScreen().frame().size.height}

def locate_btn_setting(on_retina:bool=False):
    return pyautogui.locateOnScreen(os.path.join(os.getcwd(), "images","settings.png"), grayscale=True)

def click_btn_setting(on_retina:bool=False):
    position = locate_btn_setting()
    if position is None:
      print('ERROR')
      return
    x, y = pyautogui.center(position)
    return pyautogui.click(x=x,y=y)