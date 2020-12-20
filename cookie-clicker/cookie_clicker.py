import pyautogui

pyautogui.PAUSE = 0.01

#pyautogui.displayMousePosition()
pyautogui.moveTo(x=300,y=1024)
counter = 1
while pyautogui.position() == (300,1024):
    pyautogui.click()
    counter += 1
    if counter % 200 == 0:
        pyautogui.click(x=1511,y=1157)
        pyautogui.click(x=1511,y=1357)
        pyautogui.click(x=1511,y=1557)
        pyautogui.click(x=1511,y=1757)
        pyautogui.click(x=1511,y=1957)
        pyautogui.moveTo(x=300,y=1024)
