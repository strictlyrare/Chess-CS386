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
        # Simulate pressing the Enter key to start the game
        pyautogui.press('enter')
        time.sleep(2)

        # Since we're not taking screenshots, we'll just ensure the process is still running
        # This is a basic check to verify that the game did not crash after pressing 'enter'.
        return_code = self.process.poll()
        self.assertIsNone(return_code, "The game crashed unexpectedly after pressing Enter.")

if __name__ == "__main__":
    unittest.main()
