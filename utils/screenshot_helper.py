import os
import time


def take_screenshot(driver, test_name, folder_name=None, screenshot_name='unknown'):
    if folder_name is not None:
        screenshot_dir = os.path.abspath(os.path.join(os.getcwd(), 'artifacts', 'screenshots', test_name))
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_dir = os.path.abspath(os.path.join(os.getcwd(), 'artifacts', 'screenshots', test_name, folder_name))
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.abspath(os.path.join(
            os.getcwd(),
            'artifacts',
            'screenshots',
            test_name,
            folder_name,
            f'{screenshot_name}.png')
        )
    else:
        screenshot_path = os.path.abspath(os.path.join(
            os.getcwd(),
            'artifacts',
            'screenshots',
            f'{screenshot_name}.png')
        )
    time.sleep(3)
    driver.save_screenshot(screenshot_path)
