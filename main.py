import pyautogui
import keyboard
import time

print("Welcome in AUTO-CLICKER\nby thorrow\n")
print("Click interval:")

click_interval_minutes = int(input('minutes: '))
while click_interval_minutes < 0:
    print("It cannot be less than 0")
    click_interval_minutes = int(input('minutes: '))

click_interval_seconds = int(input('seconds: '))
while click_interval_seconds < 0:
    print("It cannot be less than 0")
    click_interval_seconds = int(input('seconds: '))

click_interval_milliseconds = int(input("milliseconds: "))
while click_interval_milliseconds < 0:
    print("It cannot be less than 0")
    click_interval_milliseconds = int(input('milliseconds: '))


str_click_interval_minutes = str(click_interval_minutes).zfill(2)
str_click_interval_seconds = str(click_interval_seconds).zfill(2)
str_click_interval_milliseconds = str(click_interval_milliseconds).zfill(2)

#str_click_interval_minutes = str(click_interval_minutes)
#str_click_interval_seconds = str(click_interval_seconds)
#str_click_interval_milliseconds = str(click_interval_milliseconds)

#if len(str_click_interval_minutes) == 1:
#    str_click_interval_minutes = "0" + str_click_interval_minutes

#if len(str_click_interval_seconds) == 1:
#    str_click_interval_seconds = "0" + str_click_interval_seconds

#if len(str_click_interval_milliseconds) == 1:
#    str_click_interval_milliseconds = "0" + str_click_interval_milliseconds

mouse_button = str(input('Mouse button: ("left" or "right") ')).lower()
while mouse_button not in ["left", "right"]:
    print("Choose 'left' or 'right'")
    mouse_button = str(input('Mouse button: ("left" or "right") ')).lower()

repeat = int(input("Repeat: (times) "))

str_repeat = str(repeat)
print("\nCONFIGURATION:\nClick interval: " + str_click_interval_minutes + ":" + str_click_interval_seconds + "." + str_click_interval_milliseconds + "\nMouse button: " + mouse_button + "\nRepeat: " + str_repeat + " times")
print('\nIf you want to start the program with this configuration, click the "f8" button. To force stop click the "f9" button')

interval = click_interval_minutes * 60 + click_interval_seconds + click_interval_milliseconds / 1000

def start_clicking():
    i = 0
    while i < repeat:
        if keyboard.is_pressed('f9'):
            print("Stopping the program...")
            break
        pyautogui.click(button=mouse_button)

        elapsed = 0
        while elapsed < interval:
            if keyboard.is_pressed('f9'):
                print("Stopping the program...")
                return
            time.sleep(0.01)
            elapsed += 0.01
            
        i += 1

keyboard.wait('f8')
print("Auto-clicker started...")
start_clicking()

print("Auto-clicker finished.")