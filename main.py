"""
2021.06.16
"""

import time
import pywinmacro as pw

def sleepbye():
    pw.key_press_once("window")
    time.sleep(1)
    pw.key_press_once("tab")
    time.sleep(0.1)
    for i in range(5):
        pw.key_press_once("down_arrow")
        time.sleep(0.1)
    pw.key_press_once("enter")
    time.sleep(0.1)
    pw.key_press_once("enter")


sleepbye()
