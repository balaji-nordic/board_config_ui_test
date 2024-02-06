import pyautogui

import unittest
import subprocess
import time

class mytest(unittest.TestCase):

	def openBoardConfigurator(self):
		x, y, _, _ = pyautogui.locateOnWindow('board_controller_app.png', 'nRF Connect for Desktop v4.3.0', confidence=0.9)
		pyautogui.click(x+1300, y+100)
		time.sleep(3)

	def setUp(self):
		self.process = subprocess.Popen('C:\\Users\\basr\\AppData\\Local\\Programs\\nrfconnect\\nRF Connect for Desktop.exe')
		time.sleep(5)

	def checkBoardConfiguratorIsOpen(self) -> bool:
		try:
			x, y, _, _ = pyautogui.locateOnScreen('select_device.png', confidence=0.9)
			pyautogui.click(x,y)
			return True

		except pyautogui.ImageNotFoundException:
			return False


	def tearDown(self):
		self.process.kill()

	def test(self):
		self.openBoardConfigurator()
		self.assertTrue(self.checkBoardConfiguratorIsOpen(), "Board config UI is not detected")




if __name__ == '__main__':
    unittest.main()