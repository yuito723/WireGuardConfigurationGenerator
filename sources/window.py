# window.py

import subprocess as sp
import tkinter as tk

import common
import generator

class Window():
    def __init__(self, master):
        self.master = master

        self.master.resizable(False, False)
        self.master.iconbitmap(common.ICON_PATH)
        self.master.title(f"WireGuardConfigurationGenerator-v{common.VERSION}")
        self.master.focus_force()

        self.main()

    def main(self):
        frame = tk.Frame(self.master, padx = "5", pady = "5")
        frame.pack()

        label_0 = tk.Label(frame, font = ("Yu Gothic UI", 15, "bold"), text = "エンドポイントのアドレス")
        label_0.grid(row = 0, column = 0, padx = 5, pady = 5)
        label_1 = tk.Label(frame, font = ("Yu Gothic UI", 15, "bold"), text = "エンドポイントのポート")
        label_1.grid(row = 1, column = 0, padx = 5, pady = 5)
        label_2 = tk.Label(frame, font = ("Yu Gothic UI", 15, "bold"), text = "DNSサーバーのアドレス")
        label_2.grid(row = 2, column = 0, padx = 5, pady = 5)
        label_3 = tk.Label(frame, font = ("Yu Gothic UI", 15, "bold"), text = "ピアの数")
        label_3.grid(row = 3, column = 0, padx = 5, pady = 5)

        entry_0 = tk.Entry(frame, font = ("Yu Gothic UI", 15, "bold"))
        entry_0.grid(row = 0, column = 1, padx = 5, pady = 5)
        entry_1 = tk.Entry(frame, font = ("Yu Gothic UI", 15, "bold"))
        entry_1.grid(row = 1, column = 1, padx = 5, pady = 5)
        entry_2 = tk.Entry(frame, font = ("Yu Gothic UI", 15, "bold"))
        entry_2.grid(row = 2, column = 1, padx = 5, pady = 5)
        entry_3 = tk.Entry(frame, font = ("Yu Gothic UI", 15, "bold"))
        entry_3.grid(row = 3, column = 1, padx = 5, pady = 5)

        button_0 = tk.Button(frame, font = ("Yu Gothic UI", 15, "bold"), text = "設定ファイルを生成する", command = lambda: generator.Generator(entry_0.get(), entry_1.get(), entry_2.get(), entry_3.get()))
        button_0.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = "nsew")
        button_1 = tk.Button(frame, font = ("Yu Gothic UI", 15, "bold"), text = "終了する", command = lambda: self.master.destroy())
        button_1.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = "nsew")
        button_2 = tk.Button(frame, font = ("Yu Gothic UI", 15, "bold"), text = "出力先を開く", command = lambda: sp.run(f"explorer \"{common.DIST_PATH}\"", shell = True, capture_output = True, text = True, encoding = "shift_jis").stderr)
        button_2.grid(row = 5, column = 1, padx = 5, pady = 5, sticky = "nsew")

def app():
    app = tk.Tk()
    window = Window(app)
    app.mainloop()

if __name__ == "__main__":
    common.warning_module()
