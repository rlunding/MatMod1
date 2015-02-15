__author__ = 'Lunding'

import webbrowser
import time

breaks = 3

print("The program started on: " + time.ctime())
for i in range(0, breaks):
    time.sleep(2)
    # webbrowser.open("https://www.youtube.com/watch?v=Pecj5GGjQi8")
    print("playing video")