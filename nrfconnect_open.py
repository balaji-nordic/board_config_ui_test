import pyautogui

import unittest
import subprocess
import time
import pygetwindow


class mytest(unittest.TestCase):

    def openBoardConfigurator(self):
        x, y, w, h = pyautogui.locateOnWindow(
            'board_controller_app.png', 'nRF Connect for Desktop v4.3.0', confidence=0.9)
        x, y, _, _ = pyautogui.locateOnScreen('open.png', region=(x, y, w, h), confidence=0.9)
        pyautogui.click(x, y)
        time.sleep(3)

    def closeActiveBoardConfigurator(self):
        self.assertEqual(pygetwindow.getActiveWindowTitle(), "Board Configurator v0.1.2",
                         "Active window is not board configurator")
        pyautogui.hotkey('alt', 'f4')

    def opennRFConnectForDesktop(self):
        self.process = subprocess.Popen(
            'C:\\Users\\basr\\AppData\\Local\\Programs\\nrfconnect\\nRF Connect for Desktop.exe')
        time.sleep(5)

    def closenRFConnectForDesktop(self):
        self.process.kill()

    def setUp(self):
        self.opennRFConnectForDesktop()

    def checkBoardConfiguratorIsOpen(self) -> bool:
        try:
            x, y, _, _ = pyautogui.locateOnScreen('select_device.png', confidence=0.9)
            pyautogui.click(x, y)
            return True

        except pyautogui.ImageNotFoundException:
            return False

    def tearDown(self):
        self.closeActiveBoardConfigurator()
        self.closenRFConnectForDesktop()

    def test(self):
        self.openBoardConfigurator()
        self.assertTrue(self.checkBoardConfiguratorIsOpen(), "Board config UI is not detected")


if __name__ == '__main__':
    unittest.main()
