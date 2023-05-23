import pyautogui
import pyperclip
from time import sleep


DELAY = 3


def main():
    text = pyperclip.paste()
    print("Waiting {0} seconds and pasting {1} characters...".format(DELAY, len(text)))
    sleep(DELAY)
    pyautogui.write(text)
    print("Done.")
