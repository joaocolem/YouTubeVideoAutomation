import pyautogui
import time
import os
import pyperclip


def convert():
    variavel = r"C:\Users\joao_\PycharmProjects\pythonProject2\videox\Horoscopo Do Dia.mp4"

    pyperclip.copy(variavel)
    #pyautogui.alert("O código vai começar. Não use nada")
    #pyautogui.PAUSE = 0.5
    hand = os.startfile('C:\Program Files\HandBrake\HandBrake.exe')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('h')
    time.sleep(0.5)
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(3)

    for i in range(23):
        pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.press('up')
    for i in range(5):
        pyautogui.press('tab')
    pyautogui.press('up')
    pyautogui.hotkey('ctrl','a')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    #pyautogui.alert("Pode usar o Computador")
    for i in range(11):
        pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(900)
    pyautogui.hotkey('alt', 'f4')
    pyautogui.hotkey('alt', 'f4')

print("oi")