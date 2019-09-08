(function($) {
	setInterval(function() { 
		updatePage();
	}, 100);

	window.onload = function() {
		initDrone();
	}

})(jQuery);

function updatePage() {
	$.ajax({
		url: "/data",
		type: "GET",
		dataType: "json",
        success: function (data) {
            $("#consoleAlt").text(data.altitude);
            $("#consoleSpeed").text(data.speed);
            $("#consoleAccel").text(data.accel);
            $("#consoleBatt").text(data.battery);
        }
	});
}


var commands = ["connect", "liftOff", "findFire", "fightFire", "land"];
var info = ["> Connecting to drone...", "> Lifting off...", "> Locating fire...", "> Fighting fire...", "> Landing..."];

function initDrone() {
	sendCommand(0);
}

function sendCommand(x) {
	if (x == commands.length) {
		$("#consoleText").append("<span>> Mission complete</span><br>");
		return;
	}
	$("#consoleText").append("<span>" + info[x] + "</span><br>");
	$.ajax({
		url: "/command",
		type: "POST",
		contentType: 'application/json;charset=UTF-8',
		dataType: "json",
		data: JSON.stringify({ "command": commands[x] }),
		success: function() {
			setTimeout(sendCommand(x + 1), 20);
		}
	});
}

function liftOffAnimation() {

}