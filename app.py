import tkinter
from my_libs.helpers import activate_process, get_known_emulators
from my_libs.windows import get_screen_resolution

window = tkinter.Tk()
# screen_resolution = get_screen_resolution()

# print(screen_resolution)
# sleep(5)
# data = locate_btn_start_fishing()
# print(data)

# click_btn_setting()

# print(get_known_emulators())
known_emulators = get_known_emulators()
print(known_emulators)

activate_process(known_emulators[0].get('process_id'))
window.mainloop()
