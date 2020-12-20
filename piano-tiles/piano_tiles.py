import mss
import numpy as np
import cv2
import pyautogui
import time
import keyboard

pyautogui.PAUSE = 0.005

def take_screenshot():
    with mss.mss() as sct:
        filename = sct.shot(output='fullscreen.png')
    return filename

def get_frame(region):
    with mss.mss() as sct:
        screen = np.array(sct.grab(region))
        screen_grayscale = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        #print(screen_grayscale.shape)
        #cv2.imwrite('region.png', screen_grayscale)
    return screen_grayscale

def detect_tiles(frame):
    for x in range(frame.shape[0]):
        for y in range(frame.shape[1]):
            if frame[x,y] == 0:
                return x,y
    return None

region = {"top": 823, "left": 776, "width": 500, "height": 2}

time.sleep(3)

while True:
    if keyboard.is_pressed('q'):
        break
    start_time = time.time()
    frame = get_frame(region)
    coors = detect_tiles(frame)
    if coors:
        target_x = region['left'] + coors[1] + 1
        target_y = region['top'] + coors[0] + 1
        pyautogui.moveTo(x=target_x, y=target_y)
        pyautogui.mouseDown()
    print("%d FPS" % (1/(time.time() - start_time)))
