import platform

MAC_NAME="Darwin"
WINDOWS_NAME="Windows"
# LINUX_NAME="Linux" # No linux support

def is_mac():
  return platform.system() == MAC_NAME

def is_windows():
  return platform.system() == WINDOWS_NAME