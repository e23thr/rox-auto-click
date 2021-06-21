import platform
import wmi
from pywinauto import Application

MAC_NAME="Darwin"
WINDOWS_NAME="Windows"

KNOWN_EMULATOR_IMAGE_NAMES = ["dnplayer.exe", "HD-Player.exe"]
# LINUX_NAME="Linux" # No linux support

def is_mac():
  return platform.system() == MAC_NAME

def is_windows():
  return platform.system() == WINDOWS_NAME

def get_known_emulators():
  pl = wmi.WMI()
  process_list = [{"name":p.Name,"process_id":p.ProcessId} for p in pl.Win32_Process() if p.Name in KNOWN_EMULATOR_IMAGE_NAMES]
  del pl

  return process_list

def activate_process(process_id:int):
  app = Application().connect(process=process_id)
  app.top_window().set_focus()
  try:
    del app
  except:
    pass
