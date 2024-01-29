import pyperclip
import time
import pyautogui

message = """ضع رسالتك هنا بأي لغة
input your message here in any language
"""

with open(r"input your txt file numbers path here", "r", encoding="utf-8") as file:
    phone_numbers = file.read().splitlines()

pyautogui.hotkey("ctrl", "alt", "g")
time.sleep(2)
pyautogui.write(f"wa.me ")
pyautogui.press("enter")
time.sleep(2)
pyautogui.press("tab")
time.sleep(1)
pyautogui.press("enter")
time.sleep(2)

def send_whatsapp_message():
    for phone_number in phone_numbers:
        pyautogui.hotkey("ctrl", "alt", "g")
        time.sleep(2)
        pyautogui.write(f"wa.me/{phone_number} ")
        pyautogui.press("enter")
        time.sleep(2)
        pyperclip.copy(f"{message}")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.press("enter")


send_whatsapp_message()
