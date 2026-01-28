# common.py

import os
import subprocess as sp
import tkinter.messagebox as mb

def warning_module():
    mb.showwarning("エラー", "このプログラムはモジュールです\n単体での起動はできません")

WD_PATH = os.path.dirname(__file__)
os.chdir(WD_PATH)

TEMP_PATH = sp.run("echo %LOCALAPPDATA%\\WireGuardConfigurationGenerator", shell = True, capture_output = True, text = True, encoding = "utf-8").stdout.rstrip("\n")
sp.run(f"md \"{TEMP_PATH}\"", shell = True, capture_output = True, text = True, encoding = "shift_jis").stderr

DIST_PATH = sp.run("echo %HOMEPATH%\\WireGuardConfigurationGenerator", shell = True, capture_output = True, text = True, encoding = "utf-8").stdout.rstrip("\n")
sp.run(f"md \"{DIST_PATH}\"", shell = True, capture_output = True, text = True, encoding = "shift_jis").stderr

ICON_PATH = f"{WD_PATH}\\logo.ico"

VERSION = "1.0.0"

if __name__ == "__main__":
    warning_module()
