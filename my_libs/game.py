import os
import pyautogui
from win32api import GetSystemMetrics
import time
import random
# import win32gui
# from ctypes import windll
pyautogui.FAILSAFE = False

print("Program is running on Windows")


saved_cursor_x = 0
saved_cursor_y = 0
fishing_region = None


def get_screen_resolution():
    return {"width": GetSystemMetrics(0), "height": GetSystemMetrics(1)}


def save_mouse_position():
    global saved_cursor_x, saved_cursor_y
    position = pyautogui.position()
    saved_cursor_x = position.x
    saved_cursor_y = position.y


def set_mouse_position(x, y):
    # print(f"Set mouse position {x},{y}")
    pyautogui.moveTo(x, y)


def reset_mouse_position():
    set_mouse_position(1, 1)


def restore_mouse_position():
    global saved_cursor_x, saved_cursor_y
    set_mouse_position(saved_cursor_x, saved_cursor_y)


def locate_btn(image_name, region=None, confidence=0.5, grayscale=False):
    print(f"image_name: {image_name}")
    data = pyautogui.locateOnScreen(os.path.join(
        os.getcwd(), "images", image_name), confidence=confidence, grayscale=grayscale, region=region)
    return data


def click_on_center(position):
    x, y = pyautogui.center(position)
    pyautogui.click(x=x, y=y)


def click_btn_start_fishing():
    global fishing_region
    save_mouse_position()
    reset_mouse_position()

    position = locate_btn(image_name="start-fishing.png",
                          region=fishing_region, confidence=0.5)
    if position is None:
        restore_mouse_position()
        return False
    # if fishing_region is None:
    #     fishing_region = (position.left, position.top, position.left +
    #                       position.width, position.top+position.height)
    click_on_center(position=position)
    restore_mouse_position()
    return True


def click_btn_finish_fishing():
    global fishing_region
    save_mouse_position()
    reset_mouse_position()
    position = locate_btn(image_name="finish-fishing.png",
                          region=fishing_region, confidence=0.85, grayscale=False)
    if position is None:
        restore_mouse_position()
        return False

    click_on_center(position=position)
    restore_mouse_position()
    return True

def click_btn_start_collecting():
    save_mouse_position()
    reset_mouse_position()

    wait_position = locate_btn(image_name="wait-collecting.png", confidence=0.8)
    if wait_position is not None:
        return False;

    position = locate_btn(image_name="start-collecting.png",
                          region=fishing_region, confidence=0.9)
    if position is None:
        restore_mouse_position()
        return False
    time.sleep(random.uniform(0.2, 0.5))
    click_on_center(position=position)
    restore_mouse_position()
    return True


save_mouse_position()
