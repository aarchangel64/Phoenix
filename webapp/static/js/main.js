(function($) {
	$("#map").click(function(e) {
		xcoor = e.pageX;
		ycoor = e.pageY;
		console.log(xcoor, ycoor);
		//$('#location').append('<img src="/path/to/your/image.jpg" style="width:auto;height:auto;position:absolute;left:' + yourxcoord + ';top:'+ yourycoord +'" />");
	});

	$("#launchButton").mouseover(function() {
		console.log("fds");
		$("img").removeClass("grayscale");
	});
	$("#launchButton").mouseleave(function() {
		$("img").addClass("grayscale");
	});

})(jQuery);