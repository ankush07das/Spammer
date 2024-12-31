import os, time

os.system("pip install pyautogui")

import pyautogui

limit = 1000
initial_sleep = 5
interval = 3
spam_text = "Tui akta bhitur dim drpok!"
# click_coordinates_x, click_coordinates_y = 517, 479
# chatbox_coordinate_x, chatbox_coordinate_y = 838, 696

time.sleep(initial_sleep)

# pyautogui.moveTo(chatbox_coordinate_x, chatbox_coordinate_y)
# pyautogui.click()

for i in range(limit):
    # time.sleep(interval)
    pyautogui.write(spam_text)
    pyautogui.press('enter')

# for i in range(limit):
#     time.sleep(interval)
#     pyautogui.click(click_coordinates_x, click_coordinates_y)

# print(pyautogui.position())

os.system("pip uninstall pyautogui")