import mss
import time
import keyboard
import winsound
import pygetwindow
from PIL import Image, ImageChops


def capture_region(sct, region):
    """Captures a specified region of the screen and returns it as a PIL Image."""
    screenshot = sct.grab(region)
    return Image.frombytes('RGB', screenshot.size, screenshot.bgra, 'raw', 'BGRX')


def compare_regions(region1, region2):
    """Compares two images and returns True if a difference is detected."""
    return ImageChops.difference(region1, region2).getbbox() is not None


def beep(frequency, duration):
    """Plays a beep sound with given frequency and duration."""
    winsound.Beep(frequency, duration)


def main_loop():
    print("Press 's' to start the loop and 'q' to stop.")
    active_window = pygetwindow.getActiveWindow()  # Ensure screenshot is for the active game window
    running = False  # Flag to control the execution of the while loop
    flag_left = True  # Determines if we focus on branches on the left or right side

    # Beep parameters
    start_beep = (1000, 500)  # Frequency (Hz) and duration (ms) for start beep
    stop_beep = (2000, 500)   # Frequency (Hz) and duration (ms) for stop beep

    # Screen regions to capture
    solo_left = {'top': 710, 'left': 1120, 'width': 5, 'height': 120}
    solo_right = {'top': 710, 'left': 1430, 'width': 5, 'height': 120}

    # Multiplayer coordinates (uncomment if needed)
    # multi_left = {'top': 710, 'left': 610, 'width': 5, 'height': 120}
    # multi_right = {'top': 710, 'left': 910, 'width': 5, 'height': 120}

    with mss.mss() as sct:

        while True:
            # Start the loop if 's' is pressed and it's not running
            if keyboard.is_pressed('s') and not running:
                if active_window:
                    # Initial reference screenshots for comparison
                    pixel_left = capture_region(sct, solo_left)
                    pixel_right = capture_region(sct, solo_right)

                running = True
                print("Loop started... Press 'q' to stop.")
                beep(*start_beep)

            # Main loop logic
            while running:
                if flag_left:
                    keyboard.send('left')
                    time.sleep(0.06)
                    branch_left = capture_region(sct, solo_left)

                    # Switch direction if a change is detected on the left side
                    if compare_regions(branch_left, pixel_left):
                        flag_left = False
                else:
                    keyboard.send('right')
                    time.sleep(0.06)
                    branch_right = capture_region(sct, solo_right)

                    # Switch direction if a change is detected on the right side
                    if compare_regions(branch_right, pixel_right):
                        flag_left = True

                # Stop the loop if 'q' is pressed
                if keyboard.is_pressed('q'):
                    running = False
                    print("Loop stopped. Press 's' to start again.")
                    beep(*stop_beep)


if __name__ == '__main__':
    main_loop()
