# Python 2.7
import fire_drone
import time

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

drone = fire_drone.Drone()

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/launch', methods=['POST'])
def launch():
	return render_template("launched.html")

#Commands to drone
@app.route('/command', methods=['POST'])
def runCommand():
	command = request.get_json()['command']
	if command == "connect":
		drone.connect()
	elif command == "liftOff":
		drone.liftOff()
	elif command == "findFire":
		drone.findFire()
	elif command == "fightFire":
		drone.fightFire()
	elif command == "land":
		drone.land()
	return ('', 204)

# JSON Data from drone
@app.route('/data', methods=['GET'])
def getData():
	return '{ "altitude":"10", "speed":5, "accel":"2", "battery":"90" }'

if __name__ == '__main__':
	app.run()