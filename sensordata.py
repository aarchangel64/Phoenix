import time, sys
import ps_drone  
import json                                   # Import PS-Drone-API
import math

#drone reset, sensor config 

drone = ps_drone.Drone()                           # Start using drone
drone.startup()                                    # Connects to drone and starts subprocesses

drone.reset()                                      # Sets drone's status to good
while (drone.getBattery()[0]==-1): time.sleep(0.1) # Wait until drone has done its reset
print "Battery: "+str(drone.getBattery()[0])+"% "+str(drone.getBattery()[1]) # Battery-status
drone.useDemoMode(False)                           # Give me everything...fast
drone.getNDpackage(["demo","pressure_raw","altitude","magneto","wifi"]) # Packets to decoded
time.sleep(0.5)  
#reset #idk wat this does it was in the documentation   
drone.trim() 

#main


NDC = drone.NavDataCount
end = False
while not end:
    while drone.NavDataCount==NDC:  time.sleep(0.001) # Wait until next time-unit
    if drone.getKey():              end = True        # Stop if any key is pressed
    NDC=drone.NavDataCount
    navData = drone.NavData
    velocity = navData["demo"][4] # Get velocity vector
    speed = math.sqrt(velocity[0]**2 + velocity[1]**2 + velocity[2]**2)
    print "-----------"

    print(json.dumps("Altitude: " + str(navData["altitude"][3])))
    print(json.dumps("Battery: " + str(drone.getBattery()[0]))) #battery percentage, if battery is too low or not
    print(json.dumps("Speed: " + str(speed)))


    


    








   


