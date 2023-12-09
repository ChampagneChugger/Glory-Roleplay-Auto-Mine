import numpy as np
import mss.tools
import ctypes
import keyboard
import time
import os
import pydirectinput

# Get user screen resolution
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Possible position of blue pixels
bluepositions = [
    [57, 4],
    [68, 6],
    [77, 10],
    [85, 15],
    [93, 21],
    [98, 29],
    [103, 39],
    [105, 49],
    [105, 61],
    [103, 70],
    [99, 80],
    [94, 87],
    [87, 93],
    [79, 99],
    [70, 103],
    [62, 105],
    [54, 105],
    [45, 104],
    [37, 101],
    [30, 97],
    [22, 91],
    [16, 85],
    [12, 77],
    [8, 69],
    [6, 58],
    [6, 48],
    [9, 38],
    [13, 29],
    [17, 23],
    [23, 17],
    [30, 11],
    [37, 8],
    [45, 5],
    [51, 4],
]

boxwidth = 110
boxheight = 110

# Screenshot capture area
capturearea = {
    "top": int(screensize[1] / 2) - int(boxheight / 2),
    "left": int(screensize[0] / 2) - int(boxwidth / 2),
    "width": boxwidth,
    "height": boxheight,
}

# Array containing valid pixel positions
arrayWithBlues = []

# Clear cmd
clear = lambda: os.system("cls")


def getValidPixels():
    print("Started validating...")
    time.sleep(0.1)
    pydirectinput.mouseDown()
    time.sleep(0.1)
    pydirectinput.mouseUp()
    with mss.mss() as sct:
        img = sct.grab(capturearea)
        imgarray = np.array(img)

        for pixels in bluepositions:
            if (
                imgarray[pixels[1]][pixels[0]][0] == 194
                and imgarray[pixels[1]][pixels[0]][1] == 113
                and imgarray[pixels[1]][pixels[0]][2] == 25
            ):
                arrayWithBlues.append([pixels[1], pixels[0]])

    print("Validated...")


# Wait 4 seconds before running script
def startTimer(seconds):
    while seconds > 0:
        print("Starting in...", seconds)
        seconds -= 1
        time.sleep(1)
        clear()

    print("Started")


def doSomething():
    print("Started clicking function.")
    clicked = False
    timeout = 0
    with mss.mss() as sct:
        while clicked == False:
            img = sct.grab(capturearea)
            imgarray = np.array(img)

            timeout += 1

            if timeout > 1000:
                break

            for pixels in arrayWithBlues:
                if (
                    imgarray[pixels[0]][pixels[1]][0] == 0
                    and imgarray[pixels[0]][pixels[1]][1] == 0
                    and imgarray[pixels[0]][pixels[1]][2] == 255
                ):
                    pydirectinput.press("e")
                    clicked = True
                    print("Ended clicking function.")

    arrayWithBlues.clear()


startTimer(5)

emptyC = 0

while not keyboard.is_pressed("q"):
    if len(arrayWithBlues) == 0:
        emptyC += 1

    if emptyC > 10:
        pydirectinput.press("e")
        emptyC = 0
    elif len(arrayWithBlues) > 0:
        doSomething()
    else:
        getValidPixels()
