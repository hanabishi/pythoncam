function updateCamera() {
	var timestamp=new Date().getTime();
	$('#camera0').attr('src','webservice/cam/get_image?time='+timestamp);
}

$(document).ready(function(){
	setInterval("updateCamera();",1000);
});