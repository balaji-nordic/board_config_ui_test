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
        self.assertEqual(pygetwindow.getActiveWindowTitle(), "Board Configurator v0.1.4",
                         "Active window is not board configurator")
        pyautogui.hotkey('alt', 'f4')

    def opennRFConnectForDesktop(self):
        self.process = subprocess.Popen(
            'C:\\Users\\basr\\AppData\\Local\\Programs\\nrfconnect\\nRF Connect for Desktop.exe')
        time.sleep(5)

    def selectnrf54l15DK(self):
        x, y, _, _ = pyautogui.locateOnScreen('nrf54l15.png', confidence=0.9)
        pyautogui.click(x, y)

    def closenRFConnectForDesktop(self):
        self.process.kill()

    def checkBoardConfiguratorIsOpen(self) -> bool:
        try:
            x, y, _, _ = pyautogui.locateOnScreen('select_device.png', confidence=0.9)
            pyautogui.click(x, y)
            time.sleep(3)
            return True

        except pyautogui.ImageNotFoundException:
            return False

    def checknRF54L15ConfigurationIsShown(self) -> bool:
        try:
            x, y, _, _ = pyautogui.locateOnScreen('nRF54L15PDK.png', confidence=0.9)
            return True

        except pyautogui.ImageNotFoundException:
            return False

    def selectVoltage(self, voltage : float):
        image = f'{voltage}v.png'
        x, y, _, _ = pyautogui.locateOnScreen(image, confidence=0.8)
        pyautogui.click(x,y)
        time.sleep(2)

    def setUp(self):
        self.opennRFConnectForDesktop()

    def tearDown(self):
        self.closeActiveBoardConfigurator()
        self.closenRFConnectForDesktop()

    def test(self):
        self.openBoardConfigurator()
        self.assertTrue(self.checkBoardConfiguratorIsOpen(), "Board config UI is not detected")


if __name__ == '__main__':
    unittest.main()
