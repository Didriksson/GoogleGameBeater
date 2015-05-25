from PIL import ImageGrab
import time
import winsound
import ImageOps
import numpy as np
import win32api, win32con


screen = (510, 205, 580, 245)

#Grabbs image with the size and position of the specified box.
def grabImage(box):
	im = ImageGrab.grab(box)
	return im	

	
time.sleep(2)
bild = 1

#loop that keeps on going 'til end of program. Will grab the image and convert to a set. If the set is not all white,
#some obstacle is in the way - i.e. JUMP!
while True:
	image = grabImage(screen)
	setOFPixels = set(image.convert('L').getdata())
	if len(setOFPixels) > 1:
		image.save('bild' + str(bild) + '.jpeg', 'JPEG')
		bild = bild + 1
		win32api.keybd_event(win32con.VK_SPACE, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
		time.sleep(0.1)
		win32api.keybd_event(win32con.VK_SPACE, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
                