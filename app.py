from pyautogui import sleep
from my_libs.mac import click_btn_setting, get_screen_resolution, is_retina, locate_btn_setting
from my_libs.helpers import is_mac, is_windows

if is_mac():
    import my_libs.mac

if is_windows():
    import my_libs.windows

is_retina_screen = is_retina()
screen_resolution = get_screen_resolution()

print(screen_resolution)
sleep(3)
data = locate_btn_setting()
print(data)

click_btn_setting()