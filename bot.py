from pyautogui import *
import pyautogui
import time
import keyboard

pozicijeplavog = [
    [925, 502],
    [941, 492],
    [959, 486],
    [976, 491],
    [989, 497],
    [1001, 511],
    [1005, 552],
    [997, 569],
    [985, 581],
    [966, 587],
    [950, 588],
    [935, 583],
    [929, 577],
    [917, 566],
    [912, 557],
    [908, 543],
    [913, 516],
    [921, 504],
    [926, 499],
]


svepozplavog = []


def pozplavog():
    for x in pozicijeplavog:
        if pyautogui.pixel(x[0], x[1])[2] == 194:
            svepozplavog.extend([[x[0], x[1]]])

    print(svepozplavog)


time.sleep(4)

while keyboard.is_pressed("q") == False:
    if len(svepozplavog) == 0:
        pozplavog()

    while len(svepozplavog) != 0:
        for x in svepozplavog:
            if pyautogui.pixel(x[0], x[1])[0] == 255:
                print(x[0], x[1])
                pyautogui.keyDown("e")
                time.sleep(0.01)
                pyautogui.keyUp("e")
                svepozplavog = []
