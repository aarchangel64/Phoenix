import time
import ps_drone                # Imports the PS-Drone-API

drone = ps_drone.Drone()       # Initializes the PS-Drone-API
drone.startup()                # Connects to the drone and starts subprocesses

key = drone.getKey()


if key == "0":
	drone.takeoff()                # Drone starts
	time.sleep(7.5)  
	

	drone.stop()                   # Drone stops...
	time.sleep(2)                  # ... needs, like a car, time to stop

	drone.setSpeed(1.0)            # Sets default moving speed to 1.0 (=100%)
	print drone.setSpeed()         # Shows the default moving speed

	drone.land()                   # Drone lands

'''

drone.moveup(0.5)      
time.sleep(2)               # Gives the drone time to start


drone.moveForward()            # Drone flies forward...
time.sleep(2)                  # ... for two seconds



drone.stop()                   # Drone stops...
time.sleep(2)                  # ... needs, like a car, time to stop

drone.setSpeed(1.0)            # Sets default moving speed to 1.0 (=100%)
print drone.setSpeed()         # Shows the default moving speed

drone.land()                   # Drone lands

'''




