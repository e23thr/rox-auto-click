import os
import pyautogui
from win32api import GetSystemMetrics
# import win32gui
# from ctypes import windll

print("Program is running on Windows")


saved_cursor_x = 0
saved_cursor_y = 0


def get_screen_resolution():
    return {"width": GetSystemMetrics(0), "height": GetSystemMetrics(1)}


def save_mouse_position():
    global saved_cursor_x, saved_cursor_y
    position = pyautogui.position()
    saved_cursor_x = position.x
    saved_cursor_y = position.y


def set_mouse_position(x, y):
    print(f"Set mouse position {x},{y}")
    pyautogui.moveTo(x, y)


def reset_mouse_position():
    set_mouse_position(1, 1)


def restore_mouse_position():
    global saved_cursor_x, saved_cursor_y
    set_mouse_position(saved_cursor_x, saved_cursor_y)


def locate_btn(image_name):
    print(f"image_name: {image_name}")
    save_mouse_position()
    reset_mouse_position()
    data = pyautogui.locateOnScreen(os.path.join(
        os.getcwd(), "images", image_name), confidence=0.5)
    restore_mouse_position()
    return data


def click_on_center(position):
    x, y = pyautogui.center(position)
    pyautogui.click(x=x, y=y)


def click_btn_start_fishing():
    position = locate_btn("start-fishing.png")
    if position is None:
        return False
    click_on_center(position=position)
    return True


def click_btn_finish_fishing():
    position = locate_btn("start-fishing.png")
    if position is None:
        return False
    click_on_center(position=position)
    return True


save_mouse_position()
