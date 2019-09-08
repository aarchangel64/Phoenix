import ps_drone
import time


class Drone:
	def __init__(self):
		self.drone = ps_drone.Drone()
		self.connected = False

	def setup(self):
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
		self.connected = True

	def connect(self):
		if not self.connected:
			self.setup()

	def liftOff(self):
		self.drone.takeoff()

	def findFire(self):
		time.sleep(1)

	def fightFire(self):
		time.sleep(1)

	def land(self):
		self.drone.land()

	def fire(self):
		self.drone.startup()
		self.drone.takeoff()
		time.sleep(7.5)
		self.drone.land()
