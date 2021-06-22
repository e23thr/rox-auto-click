import sys
sys.coinit_flags = 0
import platform
import wmi
from pywinauto import Application

MAC_NAME = "Darwin"
WINDOWS_NAME = "Windows"

KNOWN_EMULATOR_IMAGE_NAMES = ["dnplayer.exe", "HD-Player.exe"]
EMULATOR_NAME_MAPPINGS = {
    "dnplayer.exe": "LD PLayer", "HD-Player.exe": "Bluestacks"
}
# LINUX_NAME="Linux" # No linux support


def is_mac():
    return platform.system() == MAC_NAME


def is_windows():
    return platform.system() == WINDOWS_NAME


def get_known_emulators():
    pl = wmi.WMI()
    # process_list = [{"name":p.Name,"process_id":p.ProcessId, "description": p.Description, "caption": p.Caption} for p in pl.Win32_Process() if p.Name in KNOWN_EMULATOR_IMAGE_NAMES]
    process_list = []
    for emulator in KNOWN_EMULATOR_IMAGE_NAMES:
        print(f"Searching for {emulator}")
        p = pl.Win32_Process(name=emulator)
        if p is not None:
            process_list.extend(p)
        else:
            print(f"{emulator} not found")
    del pl

    return process_list


def activate_process(process_id: int):
    app = Application().connect(process=process_id)
    app.top_window().set_focus()
    try:
        del app
    except:
        pass
