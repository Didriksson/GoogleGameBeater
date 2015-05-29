from PIL import ImageGrab
import time    
import winsound, cv2
import numpy as np
import win32api, win32con


gameWidth = 600
gameHeigth = 165


#Set up variables such as resolution of gamescreen etc.
def setUp():
	global gamescreen
	global checkForObstacleUpperLeft
	image = grabImage()
	posX = image.size[0]/2 - 300
	posY = 125
	gamescreen = (posX,posY, posX + gameWidth, posY + gameHeigth)
	checkForObstacleUpperLeft = (gameWidth/100 * 25, gameHeigth/100 * 70)

#Draws the box which is used to detect a tree.	
def drawRectangle(img):
	global checkForObstacleUpperLeft
	img = np.array(img)
	img = cv2.rectangle(img,checkForObstacleUpperLeft, (checkForObstacleUpperLeft[0] + 50, checkForObstacleUpperLeft[1] + 50),(255,0,0),1)
	return img

#Saves using OpenCV
def saveImage(img, path):
	cv2.imwrite(path,img)

#Grabs image with the size and position of the specified box.
def grabImage(box = None):
	im = ImageGrab.grab(box)
	return im
#Pushes space and waits 0.1 and then send command for releasing space.	
def jump():
	win32api.keybd_event(win32con.VK_SPACE, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
	time.sleep(0.1)
	win32api.keybd_event(win32con.VK_SPACE, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)

setUp()	
time.sleep(2)
bild = 1
grabImage(gamescreen).save('helabilden.jpeg', 'JPEG')

#loop that keeps on going 'til end of program. Will grab the image and convert to a set. If the set is not all white,
#some obstacle is in the way - i.e. JUMP!
while True:
	image = np.array(grabImage(gamescreen))
	box = image[checkForObstacleUpperLeft[1]:checkForObstacleUpperLeft[1]+50, checkForObstacleUpperLeft[0]:checkForObstacleUpperLeft[0]+50]
	edges = cv2.Canny(box,100,200)
	#bild = bild +1 
	if np.unique(edges).size > 1:
		#saveImage(drawRectangle(image), 'bild' + str(bild) + '.jpeg')
		#cv2.imwrite('box' + str(bild) + '.jpeg',box)
		bild = bild + 1
		jump()
		time.sleep(0.1)
                
