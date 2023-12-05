import pyautogui
import time

num_pages= int(input("How many pages is your book: "))

input("Go and collect the first page of your book then return to this. \n"
"BE SURE NOT TO CLICK ANY OTHER WINDOWS THAN KINDLE AND THIS TERMINAL!\n"
"Hit Enter Once Done...")

key_press_delay_short=0.01
key_press_delay_long=0.5

with pyautogui.hold('alt'):
    pyautogui.press('tab')

time.sleep(key_press_delay_long)


for i in range(1,num_pages):
    pyautogui.keyDown('down')  # hold down the shift key
    time.sleep(key_press_delay_long)
    pyautogui.keyUp('down')
    pyautogui.keyDown('shift')  # hold down the shift key
    time.sleep(key_press_delay_short)
    pyautogui.keyDown('prntscrn')
    time.sleep(key_press_delay_short)
    pyautogui.keyUp('prntscrn')
    time.sleep(key_press_delay_short)
    pyautogui.keyUp('shift')
    time.sleep(key_press_delay_long)
