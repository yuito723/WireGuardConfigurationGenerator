# common.py

import os
import subprocess as sp
import tkinter.messagebox as mb

def warning_module():
    mb.showwarning("エラー", "このプログラムはモジュールです\n単体での起動はできません")

PRODUCT_NAME = "WireGuardConfigurationGenerator"
VERSION = "1.0.1"

WD_PATH = os.path.dirname(__file__)
os.chdir(WD_PATH)

TEMP_PATH = sp.run(f"echo %LOCALAPPDATA%\\{PRODUCT_NAME}", shell = True, capture_output = True, text = True, encoding = "utf-8").stdout.rstrip("\n")
sp.run(f"md \"{TEMP_PATH}\"", shell = True, capture_output = True, text = True, encoding = "shift_jis").stderr

DIST_PATH = sp.run(f"echo %HOMEPATH%\\{PRODUCT_NAME}", shell = True, capture_output = True, text = True, encoding = "utf-8").stdout.rstrip("\n")
sp.run(f"md \"{DIST_PATH}\"", shell = True, capture_output = True, text = True, encoding = "shift_jis").stderr

ICON_PATH = f"{WD_PATH}\\logo.ico"

if __name__ == "__main__":
    warning_module()
