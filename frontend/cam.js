function updateCamera() {
	var timestamp=new Date().getTime();
	$('#camera0').attr('src','/webservice/camservice/get_image?cam_index=0&fake="+timestamp);
}

$(document).ready(function(){
	setInterval("updateCamera();",1000);
});