# generator.py

import subprocess as sp
import datetime

import common

class Generator():
    def __init__(self, entry_0, entry_1, entry_2, entry_3):
        self.entry_0 = str(entry_0)
        self.entry_1 = int(entry_1)
        self.entry_2 = str(entry_2)
        self.entry_3 = int(entry_3)

        self.genkey()
        self.output()

    def genkey(self):
        sp.run(f"wg genkey > \"{common.TEMP_PATH}\\endpoint.key\"", shell = True, capture_output = True, text = True, encoding = "shift_jis").stderr
        sp.run(f"type \"{common.TEMP_PATH}\\endpoint.key\" | wg pubkey > \"{common.TEMP_PATH}\\endpoint.pub\"", shell = True, capture_output = True, text = True, encoding = "shift_jis").stderr
        for i in range(self.entry_3):
            sp.run(f"wg genkey > \"{common.TEMP_PATH}\\host{i + 2}.key\"", shell = True, capture_output = True, text = True, encoding = "shift_jis").stderr
            sp.run(f"type \"{common.TEMP_PATH}\\host{i + 2}.key\" | wg pubkey > \"{common.TEMP_PATH}\\host{i + 2}.pub\"", shell = True, capture_output = True, text = True, encoding = "shift_jis").stderr
            sp.run(f"wg genkey > \"{common.TEMP_PATH}\\host{i + 2}_preshared.key\"", shell = True, capture_output = True, text = True, encoding = "shift_jis").stderr

    def output(self):
        with open(f"{common.TEMP_PATH}\\endpoint.key", "r", encoding = "utf-8") as f:
            endpoint_key = f.read().strip("\n")
        with open(f"{common.TEMP_PATH}\\endpoint.pub", "r", encoding = "utf-8") as f:
            endpoint_pub = f.read().strip("\n")
        for i in range(self.entry_3):
            with open(f"{common.TEMP_PATH}\\host{i + 2}.key", "r", encoding = "utf-8") as f:
                g = f.read().strip("\n")
                exec(f"self.host{i + 2}_key = g")
            with open(f"{common.TEMP_PATH}\\host{i + 2}.pub", "r", encoding = "utf-8") as f:
                g = f.read().strip("\n")
                exec(f"self.host{i + 2}_pub = g")
            with open(f"{common.TEMP_PATH}\\host{i + 2}_preshared.key", "r", encoding = "utf-8") as f:
                g = f.read().strip("\n")
                exec(f"self.host{i + 2}_preshared_key = g")

        wg0 = f"""
#endpoint1
[Interface]
Address = 10.0.0.1/24
ListenPort = {self.entry_1}
DNS = {self.entry_2}
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE
PrivateKey = {endpoint_key}
""".lstrip("\n")

        for i in range(self.entry_3):
            exec(f"self.host_pub = self.host{i + 2}_pub")
            exec(f"self.host_preshared_key = self.host{i + 2}_preshared_key")
            wg0 += f"""
#host{i + 2}
[Peer]
AllowedIPs = 10.0.0.{i + 2}/32
PublicKey = {self.host_pub}
PresharedKey = {self.host_preshared_key}
"""

        with open(f"{common.TEMP_PATH}\\wg0.conf", "w", encoding = "utf-8") as f:
            f.write(wg0)

        for i in range(self.entry_3):
            exec(f"self.host_key = self.host{i + 2}_key")
            exec(f"self.host_preshared_key = self.host{i + 2}_preshared_key")
            host = f"""
#host{i + 2}
[Interface]
Address = 10.0.0.{i + 2}/24
DNS = {self.entry_2}
PrivateKey = {self.host_key}

[Peer]
AllowedIPs = 10.0.0.0/24
Endpoint = {self.entry_0}:{self.entry_1}
PublicKey = {endpoint_pub}
PresharedKey = {self.host_preshared_key}
PersistentKeepalive = 25
""".lstrip("\n")

            with open(f"{common.TEMP_PATH}\\host{i + 2}.conf", "w", encoding = "utf-8") as f:
                f.write(host)

        time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        sp.run(f"md \"{common.DIST_PATH}\\{time}\"", shell = True, capture_output = True, text = True, encoding = "shift_jis").stderr
        sp.run(f"move \"{common.TEMP_PATH}\\*.conf\" \"{common.DIST_PATH}\\{time}\"", shell = True, capture_output = True, text = True, encoding = "shift_jis").stderr
        sp.run(f"del /s /q /f \"{common.TEMP_PATH}\\*.key\" \"{common.TEMP_PATH}\\*.pub\"", shell = True, capture_output = True, text = True, encoding = "shift_jis").stderr

if __name__ == "__main__":
    common.warning_module()
