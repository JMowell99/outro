import time
import os

x = 11
i = 0
time.sleep(6.5)
for _ in range(10):
    x = x - 1
    print(f"Shutting down computer in {x} seconds")
    time.sleep(1)
print("It's show time")
time.sleep(2)
os.system('sleep.bat')