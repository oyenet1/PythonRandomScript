#!/usr/bin/env python3

import pyautogui as p
import time

time.sleep(5)

for i in range(100):
    p.typewrite("Are you ready")
    p.press("enter")
