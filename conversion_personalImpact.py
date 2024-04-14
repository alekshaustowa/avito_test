import playwright
import pyscreenshot
from PIL import ImageGrab
import pyautogui, time

time.sleep(3)
#image = pyautogui.screenshot()
#image.save('screen.png')

image = ImageGrab.grab()
image.save('testcases3.8.png')