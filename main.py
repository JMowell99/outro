import os
from playsound import playsound

os.system('start "" /MAX "cmd /K python countdown.py && exit()')
playsound('./sound.mp3')