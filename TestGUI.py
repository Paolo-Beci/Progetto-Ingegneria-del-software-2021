
from asyncio import subprocess
import pyautogui
import time
import subprocess
import multiprocessing
from home.view.VistaHome import VistaHome
import sys
from PyQt5.QtWidgets import QApplication

################## TEST #################

# Metodo che esegue il gestionale
def runProgram():
    subprocess.run(["python3.8", 'main.py'])

# metodo che esegue i test di interfaccia
def runTest():
    time.sleep(6)
    test_login()
    

def test_login():
    #coordinate centrali del pulsante login
    login_button_coords= pyautogui.locateCenterOnScreen('immagini_test/login_button.png')
    

    

    #mi sposto sul pulsante login
    pyautogui.moveTo(login_button_coords.x, login_button_coords.y, 1)
    #lo clicco
    pyautogui.click(login_button_coords)
    time.sleep(0.5)

    #coordinate centrali della form username
    user_form_coords= pyautogui.locateCenterOnScreen('immagini_test/user_form.png')
    #mi sposto sulla form username
    pyautogui.moveTo(user_form_coords.x, user_form_coords.y, 1)
    #la clicco
    pyautogui.click(user_form_coords)
    time.sleep(0.5)
    #scrivo l'username
    pyautogui.write("prof", 0.5)
    #coordinate centrali della form password
    pass_form_coords= pyautogui.locateCenterOnScreen('immagini_test/pass_form.png')
    #mi sposto sulla form password
    pyautogui.moveTo(pass_form_coords.x, pass_form_coords.y, 0.5)
    #ci clicclo
    pyautogui.click(pass_form_coords)
    time.sleep(0.5)
    #scrivo la password
    pyautogui.write("prof", 0.5)

    #coordinate centrali del pulsante accedi
    loginto_button_coords= pyautogui.locateCenterOnScreen('immagini_test/loginto_button.png')
    #mi sposto sul pulsante di accesso
    pyautogui.moveTo(loginto_button_coords.x, loginto_button_coords.y, 0.5)
    #lo clicclo
    pyautogui.click(loginto_button_coords)

# Creo due multi-processi
p1= multiprocessing.Process(target=runProgram)
p2= multiprocessing.Process(target=runTest)

# Avvio i due processi in parallelo
p1.start()
p2.start()