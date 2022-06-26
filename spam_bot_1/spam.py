import pyautogui, time, keyboard, pywinauto

time.sleep(5)
f = open('text_2','r')  #Открываем файл для чтения



for line in f:
    if not keyboard.is_pressed('space'):

        time.sleep(0.5)
        pyautogui.typewrite(line)
        pyautogui.press('enter')

    else:
        break



# from keyboard import press_and_release
# from time import sleep
# import pyautogui, pyperclip
#
# def paste(text: str):
#     pyperclip.copy(text)
#     press_and_release('ctrl + v')
#
#
# def type(text: str, interval=0.0):
#     buffer = pyperclip.paste()
#     if not interval:
#         paste(text)
#     else:
#         for char in text:
#             paste(char)
#             sleep(interval)
#     pyperclip.copy(buffer)


# pyautogui.hotkey('Win')
# type('Привет мир!', 0.1)
# from keyboard import press_and_release
# from time import sleep
# import pyautogui, pyperclip
#
# def paste(text: str):
#     pyperclip.copy(text)
#     press_and_release('ctrl + v')
#
#
# def type(text: str, interval=0.0):
#     buffer = pyperclip.paste()
#     if not interval:
#         paste(text)
#     else:
#         for char in text:
#             paste(char)
#             sleep(interval)
#     pyperclip.copy(buffer)
# keyboard.press_and_release('ctrl + v')
#
# pyautogui.hotkey('Win')
# type('Привет мир!', 0.1)



# import pyautogui, pyperclip, keyboard
#
# def paste(text: str):
#     buffer = pyperclip.paste()
#     pyperclip.copy(text)
#     keyboard.press_and_release('ctrl + v')
#     pyperclip.copy(buffer)
#
#
# pyautogui.hotkey('Win')
# paste("Привет мир!")