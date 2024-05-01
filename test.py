import subprocess
import platform

def open_command_prompt():
    # İşletim sistemini kontrol et
    operating_system = platform.system()

    # İşletim sistemine göre komut istemcisini aç
    if operating_system == 'Windows':
        subprocess.call('cmd', shell=True)
    elif operating_system == 'Linux':
        subprocess.call('gnome-terminal', shell=True)
    elif operating_system == 'Darwin':  # macOS
        subprocess.call('Terminal', shell=True)
    else:
        print("İşletim sistemi desteklenmiyor.")

# Komut istemcisini aç
open_command_prompt()
