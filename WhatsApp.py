import time
import pyautogui
import pyperclip

message = """
مرحباً، كيف حالك؟
أريد منك أموال
red flag
"""


def send_whatsapp_message():
    with open(
        r"E:\Projects\Coding\pythonProjects\numbers.txt", "r", encoding="utf-8"
    ) as file:
        phone_numbers = file.read().splitlines()
    time.sleep(2)
    for phone_number in phone_numbers:
        pyautogui.hotkey("winleft")
        time.sleep(1)
        pyautogui.write("Google Chrome")
        pyautogui.press("enter")
        time.sleep(1)
        time.sleep(2)

        formatted_message = message.replace("\n", "%0A")

        pyperclip.copy(f"https://wa.me/{phone_number}?text={formatted_message}")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        pyautogui.press("enter")
        time.sleep(5)
        pyautogui.press("enter")
        pyautogui.press("enter")
        time.sleep(5)


send_whatsapp_message()
