import base64
import math
import cv2
import ps_drone
import time
import PhoenixVision

class Drone:
	def __init__(self):
		self.drone = ps_drone.Drone()
		self.connected = False
		self.altitude = 0
		self.speed = 0
		self.accel = 0
		self.battery = 0

	def __setup(self):
		# drone reset, sensor config
		self.drone.startup()  # Connects to drone and starts subprocesses

		self.drone.reset()  # Sets drone's status to good
		while self.drone.getBattery()[0] == -1: time.sleep(0.1)  # Wait until drone has done its reset
		print("Battery: " + str(self.drone.getBattery()[0]) + "% " + str(self.drone.getBattery()[1]))  # Battery-status
		self.drone.useDemoMode(True)
		self.drone.getNDpackage(["demo", "altitude"])  # Packets to decoded
		time.sleep(0.5)
		# reset #idk wat this does it was in the documentation
		self.drone.trim()
		self.drone.setConfigAllID()  # Go to multiconfiguration-mode
		self.drone.sdVideo()  # Choose lower resolution (hdVideo() for...well, guess it)
		self.drone.frontCam()  # Choose front view
		CDC = self.drone.ConfigDataCount
		while CDC == self.drone.ConfigDataCount: time.sleep(0.0001)  # Wait until it is done (after resync is done)
		#self.getNavData()
		self.drone.startVideo()  # Start video-function
		self.drone.showVideo()
		self.connected = True

	def __gcp_detect(self):
		IMC = self.drone.VideoImageCount
		fire_detected = False

		while not fire_detected:
			while self.drone.VideoImageCount == IMC: time.sleep(0.01)  # Wait until the next video-frame
			IMC = self.drone.VideoImageCount
			img = self.drone.VideoImage
			# Convert img to base64
			retval, buffer = cv2.imencode('.jpg', img)
			img64 = base64.b64encode(buffer)
			fire_detected = PhoenixVision.detect_image(img64)

	def connect(self):
		if not self.connected:
			self.__setup()

	def getNavData(self):
		navData = self.drone.NavData
		self.altitude = navData["altitude"][3]
		self.battery = self.drone.getBattery()[0]
		velocity = navData["demo"][4]  # Get velocity vector
		self.speed = math.sqrt(velocity[0] ** 2 + velocity[1] ** 2 + velocity[2] ** 2)

	def liftOff(self):
		self.drone.takeoff()
		time.sleep(8)  # Time required for the drone to takeoff, as drone functions are non-blocking

	def findFire(self):
		self.drone.turnRight(0.5)
		self.__gcp_detect()  # Blocks until fire has been detected
		self.drone.stop()
		time.sleep(1)  # Wait for the drone to stop

	def fightFire(self):
		return

	def land(self):
		self.drone.land()
		time.sleep(8)  # Time required for the drone to land, as drone functions are non-blocking
