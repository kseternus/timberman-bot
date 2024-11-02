import mss
import time
import keyboard
import winsound
import pygetwindow
from PIL import Image, ImageChops


def capture_region(sct, region):
    """Capture a specified region of the screen and return it as a PIL Image."""
    screenshot = sct.grab(region)
    return Image.frombytes('RGB', screenshot.size, screenshot.bgra, 'raw', 'BGRX')


def regions_differ(region1, region2):
    """Return True if two images differ."""
    return ImageChops.difference(region1, region2).getbbox() is not None


def beep_sound(frequency, duration):
    """Play a beep sound with given frequency and duration."""
    winsound.Beep(frequency, duration)


def get_game_settings():
    """Prompt the user to select a game mode and return the screen capture settings."""
    game_modes = {
        1: ('Solo mode', 1120, 1430, 720, 5, 120),
        2: ('Two players online mode', 610, 910, 720, 5, 120),
        3: ('Four/Eight players online mode', 355, 525, 940, 5, 120)
    }

    while True:
        try:
            choice = int(input('Select game mode:\n'
                               '1) Solo game\n'
                               '2) Online two players mode\n'
                               '3) Online four/eight players mode\n'
                               ': '))
            if choice in game_modes:
                mode_name, x1, x2, y, width, height = game_modes[choice]
                print(f'Selected {mode_name}')
                return x1, x2, y, width, height
            else:
                print('Invalid choice. Please select 1, 2, or 3.')
        except ValueError:
            print('Invalid input. Please enter a number.')


def run_main_loop(x1, x2, y, width, height):
    """Main loop that monitors screen regions and controls keyboard inputs."""
    print("\nPress 's' to start the loop and 'q' to stop.")
    active_window = pygetwindow.getActiveWindow()

    running = False
    direction_left = True

    start_beep = (1000, 500)
    stop_beep = (2000, 500)

    regions = {
        'left': {'top': y, 'left': x1, 'width': width, 'height': height},
        'right': {'top': y, 'left': x2, 'width': width, 'height': height}
    }

    with mss.mss() as sct:
        while True:
            if keyboard.is_pressed('s') and not running:
                if active_window:
                    reference_left = capture_region(sct, regions["left"])
                    reference_right = capture_region(sct, regions["right"])
                running = True
                print("\nLoop started... Press 'q' to stop.")
                beep_sound(*start_beep)

            while running:
                current_side = "left" if direction_left else "right"
                keyboard.send(current_side)
                time.sleep(0.06)

                region_capture = capture_region(sct, regions[current_side])
                reference_capture = reference_left if direction_left else reference_right

                if regions_differ(region_capture, reference_capture):
                    direction_left = not direction_left

                if keyboard.is_pressed('q'):
                    running = False
                    print("\nLoop stopped. Press 's' to start again.")
                    beep_sound(*stop_beep)


if __name__ == '__main__':
    x1, x2, y, width, height = get_game_settings()
    run_main_loop(x1, x2, y, width, height)
