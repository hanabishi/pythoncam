function updateCamera(cameraIndex) {
	if(window.shutdown!=1) {
		var timestamp=new Date().getTime();
		$('#camera'+cameraIndex).attr('src','webservice/camservice/get_image?cam_index='+cameraIndex+'&fake='+timestamp);

	}
}

$(document).ready(function(){
	window.shutdown=0;
	$.getJSON("webservice/camservice/get_cameras",function(camserviceData){
		cameraIndexes=camserviceData['cameraIndexes'];
		$('#main').html("");
		for(cameraIndex in cameraIndexes) {
			$('body #main').append('<img src="loading.jpg" id="camera'+cameraIndexes[cameraIndex]+'" class="camera_mini" />');
			setInterval("updateCamera("+ cameraIndexes[cameraIndex]+");",1000);
		}
	}).fail(function() {
		$('#main').html("We suck!");
	});

	$("#shutdown").on('click',function() {
		window.shutdown=1;
		$.get('shutdown');
	});
});