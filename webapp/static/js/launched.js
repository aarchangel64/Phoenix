(function($) {
	setInterval(function() { 
		updatePage();
	}, 3000);

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
            console.log(JSON.stringify(data));
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
		return;
	}
	$("#consoleText").append("<span>" + info[x] + "</span><br>");
	$.ajax({
			url: "/command",
			type: "POST",
			data: commands[x],
			success: function(){
				setTimeout(sendCommand(x + 1), 20);
			}
		});
}

function liftOffAnimation() {

}