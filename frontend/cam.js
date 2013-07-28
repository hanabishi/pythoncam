function updateCamera(cameraIndex) {
	var timestamp=new Date().getTime();
	$('#camera0').attr('src','webservice/camservice/get_image?cam_index='+cameraIndex+'&fake='+timestamp);
}

$(document).ready(function(){
	$.getJSON("webservice/camservice/get_cameras",function(camserviceData){
		cameraCount=camserviceData['cameraCount'];
		for(cameraIndex=0;cameraIndex<cameraCount;cameraIndex++) {
			$('body').append('<img src="loading.jpg" id="camera'+cameraIndex+'" />');
			setInterval("updateCamera("+cameraIndex+");",1000);
		}
		$('#initialLoad').remove();
	}).fail(function() {
		$('#initialLoad').html("We suck!");
	});
	
});