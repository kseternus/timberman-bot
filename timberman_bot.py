import mss
import time
import keyboard
import winsound
import pygetwindow
from PIL import Image, ImageChops


def main_loop():
    running = False  # Flag to control the execution of the while loop
    flag_left = True  # Flag to know if whether we ignore the branches on the left or right side
    print("Press 's' to start the loop and 'q' to stop.")
    active_window = pygetwindow.getActiveWindow()  # Ensure we screenshot game window not IDE or wallpaper

    # Frequency is in Hertz (Hz), Duration is in milliseconds (ms)
    frequency = 1000  # Frequency of the beep (1000 Hz)
    frequency2 = 2000  # Frequency of the beep (2000 Hz)
    duration = 500  # Duration of the beep (500 ms)

    with mss.mss() as sct:
        while True:
            # Check if 's' is pressed to start the loop
            if keyboard.is_pressed('s') and not running:
                if active_window:
                    # Initial background screenshots (outside the loop)
                    # These coordinates are for 2500x1600 resolution
                    # Capture a region of the screen as a starting point for comparison
                    # solo
                    pixel_left = sct.grab({'top': 710, 'left': 1120, 'width': 5, 'height': 120})
                    # multiplayer 2
                    # pixel_left = sct.grab({'top': 710, 'left': 610, 'width': 5, 'height': 120})
                    pixel_left = Image.frombytes('RGB', pixel_left.size, pixel_left.bgra, 'raw',
                                                 'BGRX')
                    # solo
                    pixel_right = sct.grab({'top': 710, 'left': 1430, 'width': 5, 'height': 120})
                    # multiplayer 2
                    # pixel_right = sct.grab({'top': 710, 'left': 910, 'width': 5, 'height': 120})
                    pixel_right = Image.frombytes('RGB', pixel_right.size, pixel_right.bgra, 'raw',
                                                  'BGRX')
                running = True
                print("Loop started... Press 'q' to stop.")
                # Play beep to inform about start
                winsound.Beep(frequency, duration)

            # If the loop is running, execute the main logic
            if running:
                if flag_left:
                    # Continuously click the left key
                    keyboard.send('left')
                    time.sleep(0.06)
                    # Capture screen area for comparison
                    # solo
                    branch_left = sct.grab({'top': 710, 'left': 1120, 'width': 5, 'height': 120})
                    # multiplayer 2
                    # branch_left = sct.grab({'top': 710, 'left': 610, 'width': 5, 'height': 120})
                    branch_left = Image.frombytes('RGB', branch_left.size, branch_left.bgra, 'raw',
                                                  'BGRX')
                    # If a difference is detected, switch to the right
                    if ImageChops.difference(branch_left, pixel_left).getbbox():
                        flag_left = False

                else:
                    # Continuously click the right key
                    keyboard.send('right')
                    time.sleep(0.06)
                    # Capture screen area for comparison
                    # solo
                    branch_right = sct.grab({'top': 710, 'left': 1430, 'width': 5, 'height': 120})
                    # multiplayer 2
                    # branch_right = sct.grab({'top': 710, 'left': 910, 'width': 5, 'height': 120})
                    branch_right = Image.frombytes('RGB', branch_right.size, branch_right.bgra, 'raw',
                                                   'BGRX')
                    # If a difference is detected, switch to the left
                    if ImageChops.difference(branch_right, pixel_right).getbbox():
                        flag_left = True

            # Check if 'q' is pressed to stop the loop
            if keyboard.is_pressed('q') and running:
                running = False
                print("Loop stopped. Press 's' to start again.")
                # Play beep to inform about stop
                winsound.Beep(frequency2, duration)


if __name__ == '__main__':
    main_loop()
