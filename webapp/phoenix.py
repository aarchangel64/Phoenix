# Python 2.7
import drone
import json
import time

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/launch', methods=['POST'])
def launch():
	return render_template("launched.html")

#Commands to drone
@app.route('/command', methods=['POST'])
def runCommand():
	print "hello"
	time.sleep(2)
	print request.data
	return
	#drone.connect()

	#drone.liftOff()
	#drone.findFire()
	#drone.fightFire()
	#drone.land()

# JSON Data from drone
@app.route('/data', methods=['GET'])
def getData():
	return '{ "name":"John", "age":30, "city":"New York"}'

if __name__ == '__main__':
	app.run()