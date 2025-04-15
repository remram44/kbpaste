import pyautogui
import pyperclip
from time import sleep


DELAY = 3


def write(message, interval=0.0):
    last_upper = False
    for c in message:
        upper = c.isupper()
        c = c.lower()

        if c == '<':
            upper = True
            c = ','

        if upper and not last_upper:
            pyautogui.keyDown('shift')
            sleep(interval)
        elif not upper and last_upper:
            pyautogui.keyUp('shift')
            sleep(interval)
        last_upper = upper

        pyautogui.keyDown(c)
        sleep(interval)
        pyautogui.keyUp(c)
        sleep(interval)


def main():
    text = pyperclip.paste()
    print("Waiting {0} seconds and pasting {1} characters...".format(DELAY, len(text)))
    sleep(DELAY)
    write(text, interval=0.01)
    print("Done.")
