import subprocess
import time
import psutil

Process = subprocess.Popen("notepad,exe")
time.sleep(2)
Process_info = Psutil.Process(Process.pid)
print("Process ID:", Process.pid)
print("Processing priority: ",Process_info.nice())
Process.wait()
print("Process with ID: ",Process.pid,"completed")