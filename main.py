import os
from playsound import playsound

os.system('start "" /MAX "cmd /K python countdown.py && exit()')
playsound('./sound.mp3')
os.system('rundll32.exe powrprof.dll, SetSuspendState Sleep')