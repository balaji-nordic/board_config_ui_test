import pyautogui

import unittest
import subprocess
import time
import pygetwindow
from PIL import Image

class mytest(unittest.TestCase):

    def resize(self, filename:str):
        img = Image.open(filename)
        resized_board_controller_img = img.resize((int(img.size[0]*self.scaling[0]), int(img.size[1]*self.scaling[1])), resample=Image.Resampling.LANCZOS)
        resized_board_controller_img.save(f'resized_{filename}')

    def __init__(self, methodName: str = "runTest") -> None:
        self.confidence = 0.9

        current_size = pyautogui.size()
        orig_size = (1920, 1080) # Size of the screen in which original images were taken.
        self.scaling = (current_size[0]/orig_size[0], current_size[1]/orig_size[1])
        self.resize('open.png')
        self.resize('board_controller_app.png')
        self.resize('select_device.png')
        #TODO : Resize the rest of the image
        super().__init__(methodName)

    def openBoardConfigurator(self):
        x, y, w, h = pyautogui.locateOnWindow(
            'resized_board_controller_app.png', 'nRF Connect for Desktop v4.3.0', confidence=self.confidence)
        x, y, _, _ = pyautogui.locateOnScreen('resized_open.png', region=(x, y, w, h), confidence=self.confidence)
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
        x, y, _, _ = pyautogui.locateOnScreen('nrf54l15.png', confidence=self.confidence)
        pyautogui.click(x, y)

    def closenRFConnectForDesktop(self):
        self.process.kill()

    def checkBoardConfiguratorIsOpen(self) -> bool:
        x, y, _, _ = pyautogui.locateOnScreen('resized_select_device.png', confidence=self.confidence)
        pyautogui.click(x, y)
        time.sleep(3)

    def checknRF54L15ConfigurationIsShown(self) -> bool:
        try:
            x, y, _, _ = pyautogui.locateOnScreen('nRF54L15PDK.png', confidence=self.confidence)
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
