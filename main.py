import cv2
import numpy as np
import pyautogui
import time

SCREEN_SIZE = (1920, 1080)  # (width, height)

fourcc = cv2.VideoWriter_fourcc(*'XVID')    # Define the codec and create VideoWriter object
out = cv2.VideoWriter('output.avi', fourcc, 20.0, SCREEN_SIZE)  # Define the output file

fps = 120   # frames per second
prev = 0    # previous time

while True:

    time_elapsed = time.time() - prev   # time elapsed since last frame

    img = pyautogui.screenshot()    # get image from screen

    if time_elapsed > 1/fps:       # if time elapsed is greater than 1/fps
        prev = time.time()  # update prev
        frame = np.array(img)   # convert image to numpy array
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # convert to RGB
        out.write(frame)    # write the frame to file

    cv2.waitKey(100)  # wait 1ms

cv2.destroyAllWindows() # close all opencv windows
out.release()   # release the file
