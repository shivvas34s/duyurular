import subprocess

def start_chrome():
    subprocess.Popen(["start", "chrome"], shell=True)

# Chrome'u başlat
start_chrome()
