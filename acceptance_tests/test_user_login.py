import unittest
import subprocess
import time
import pyautogui

class TestUserLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Start the Pygame application as a subprocess
        cls.process = subprocess.Popen(["python", "main.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(5)  # Wait for the application to start

    @classmethod
    def tearDownClass(cls):
        # Terminate the Pygame subprocess
        cls.process.terminate()
        cls.process.wait()

    def test_valid_login(self):
        # Assuming the login window is active upon launch
        username = "valid_user"
        password = "valid_password"

        # Enter the username
        pyautogui.write(username, interval=0.1)
        pyautogui.press('enter')

        # Enter the password
        pyautogui.write(password, interval=0.1)
        pyautogui.press('enter')

        # Wait for login process to complete
        time.sleep(2)

        # Since there's no screenshot, we check if the application didn't crash
        return_code = self.process.poll()
        self.assertIsNone(return_code, "The application crashed unexpectedly after attempting login.")

    def test_invalid_login(self):
        # Assuming the login window is active upon launch
        username = "invalid_user"
        password = "invalid_password"

        # Enter the username
        pyautogui.write(username, interval=0.1)
        pyautogui.press('enter')

        # Enter the password
        pyautogui.write(password, interval=0.1)
        pyautogui.press('enter')

        # Wait for login process to complete
        time.sleep(2)

        # Assuming the application displays an error message, we do not expect a crash
        return_code = self.process.poll()
        self.assertIsNone(return_code, "The application crashed unexpectedly after attempting login with invalid credentials.")

if __name__ == "__main__":
    unittest.main()
