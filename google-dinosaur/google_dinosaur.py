import mss
import cv2
import numpy as np
import keyboard
import pyautogui
import time

pyautogui.PAUSE = 0.01

def take_screenshot():
    with mss.mss() as sct:
        filename = sct.shot(output='fullscreen.png')
    return filename

def get_frame(region):
    with mss.mss() as sct:
        screen = np.asarray(sct.grab(region))
        screen_grayscale = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        #print(screen_grayscale.shape)
        #cv2.imwrite("region.png",screen_grayscale)
    return screen_grayscale

def paint_lines(region):
    with mss.mss() as sct:
        full_screen = {"top": 0, "left": 0,"width": 3840, "height": 2160}
        screen = np.asarray(sct.grab(full_screen))
        screen_grayscale = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        for i in [region['top'], region['top'] + 70]:
            for j in range(region['left'], region['left'] + region['width']):
                screen_grayscale[i,j] = 130
    cv2.imwrite("region_on_screen.png", screen_grayscale)

def collision_detected(frame):
    for x in [0, 70]:
        if len(set(frame[x])) > 2:
            return True
    return False

region = {"top": 1150, "left": 300, "width": 350, "height": 85}

prev_time = time.time()
while True:
    if keyboard.is_pressed('q'):
        break
    start_time = time.time()
    if start_time - prev_time >= 2:
        if region['width'] < 1600: region['width'] += 13
        prev_time = start_time
    frame = get_frame(region)
    if collision_detected(frame):
        pyautogui.keyDown('space')
    print("%d FPS" % (1/(time.time() - start_time)))