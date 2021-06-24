from my_libs.game import click_btn_finish_fishing, click_btn_start_collecting, click_btn_start_fishing, reset_mouse_position
import tkinter as tk
from datetime import datetime, timedelta
from my_libs.helpers import get_known_emulators, EMULATOR_NAME_MAPPINGS

window = tk.Tk()
DEFAULT_STATUS = "กรุณาเปิด Emulator/เข้าเกม/อยู่ที่จุดเริ่มตกปลาหรือเก็บเกี่ยว"
ACTION_FISHING = "fishing"
ACTION_COLLECTING = "collecting"
TEXT_FISHING = "ตกปลา"
TEXT_COLLECTING = "เก็บเกี่ยว"
DEFAULT_TIME = "360"
action = ""
working = False
btn_fishing = None
btn_collecting = None

lbl_status = None
fishing_started = False

ent_counter = None
end_time = datetime.now()
fishing_counter = 0


def action_loop():
    global action, working, window, fishing_started, lbl_status, ent_counter, fishing_counter

    if end_time < datetime.now():
        working = False
        update_btn_state()
        print("End job")
        lbl_status.configure(text="จบการทำงาน")

    if working:
        if action == ACTION_COLLECTING:
            click_btn_start_collecting()

        if action == ACTION_FISHING:
            fishing_counter = fishing_counter + 1
            if fishing_counter % 20 == 0:
                click_btn_start_fishing()
            click_btn_finish_fishing()

        window.after(5, action_loop)


def update_btn_state():
    global action, working, btn_fishing, btn_collecting, lbl_status

    if not working:
        btn_collecting.config(state="normal")
        btn_fishing.config(state="normal")
        btn_collecting.configure(text=f"เริ่ม{TEXT_COLLECTING}")
        btn_fishing.configure(text=f"เริ่ม{TEXT_FISHING}")
        lbl_status.configure(text=DEFAULT_STATUS)
        return

    if action == ACTION_FISHING:
        btn_collecting.config(state="disabled")
        btn_fishing["text"] = f"หยุด{TEXT_FISHING}"

    if action == ACTION_COLLECTING:
        btn_fishing.config(state="disabled")
        btn_collecting["text"] = f"หยุด{TEXT_COLLECTING}"


def go_fishing(event):
    global action, working, btn_fishing, end_time

    if str(btn_fishing["state"]) == "disabled":
        return
    end_time = datetime.now() + timedelta(seconds=int(ent_counter.get()))
    action = ACTION_FISHING
    working = True
    update_btn_state()
    action_loop()


def go_collecting(event):
    global action, working, btn_collecting, end_time

    if str(btn_collecting["state"]) == "disabled":
        return

    end_time = datetime.now() + timedelta(seconds=int(ent_counter.get()))
    action = ACTION_COLLECTING
    working = True
    update_btn_state()
    action_loop()


def create_ui(app):
    global btn_fishing, btn_collecting, lbl_status, ent_counter

    known_emulators = get_known_emulators()
    emulator_names = [EMULATOR_NAME_MAPPINGS[e.Name] for e in known_emulators]
    selected_emulator = tk.StringVar(app)
    selected_emulator.set(emulator_names[0] if len(emulator_names) > 0 else "")

    tk.Label(text="เลือก Emulator").grid(row=0, column=0, sticky="ew")
    tk.OptionMenu(app, selected_emulator, *emulator_names).grid(row=0,
                                                                column=1, sticky="ew", columnspan=3)

    ent_counter = tk.Entry()
    ent_counter.insert(0, DEFAULT_TIME)
    ent_counter.grid(row=1, column=0, columnspan=4, sticky="ew")

    btn_fishing = tk.Button(text=f"เริ่ม{TEXT_FISHING}")
    btn_fishing.grid(row=2, column=0, sticky="ew", columnspan=2)
    btn_fishing.bind("<Button-1>", go_fishing)
    btn_collecting = tk.Button(text=f"เริ่ม{TEXT_COLLECTING}")
    btn_collecting.grid(row=2, column=2, sticky="ew", columnspan=2)
    btn_collecting.bind("<Button-1>", go_collecting)

    lbl_status = tk.Label(text=DEFAULT_STATUS)
    lbl_status.grid(row=3, column=0, columnspan=4, sticky="w")


if __name__ == "__main__":
    window.rowconfigure(0, minsize=50)
    window.columnconfigure([0, 1, 2, 3], minsize=150)
    create_ui(window)

    window.mainloop()
