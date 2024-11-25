import unittest
import subprocess
import time
import pyautogui

class TestPygameAcceptance(unittest.TestCase):

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

    def test_start_game(self):
        # Assuming that the application is focused on launch
        # Simulate pressing the Enter key to start the game
        pyautogui.press('enter')
        time.sleep(2)

        # Check if a specific element has changed (e.g., a game board is displayed)
        # This can be verified by taking a screenshot and locating certain expected components
        screenshot = pyautogui.screenshot()
        screenshot.save("acceptance_test_screenshot.png")

        # Optionally, perform image analysis using PyAutoGUI's image recognition features
        # For example, check if a chess piece appears in the screenshot
        piece_found = pyautogui.locateOnScreen("images/pieces/wp.png")
        self.assertIsNotNone(piece_found, "The game did not start as expected; could not find the chess piece on the screen.")

if __name__ == "__main__":
    unittest.main()
