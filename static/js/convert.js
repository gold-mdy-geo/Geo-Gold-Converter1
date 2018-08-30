$(document).ready(function(){
	$('form').on('submit', function(event){
		$.ajax({
			type: "POST",
			url: "/convert",
			success: function(response){
				console.log(response);
			},
			data: {
				myinput: $('label[for=source]').html(),
				myoutput: $('label[for=destination]').html(),
				source: $('#source').val()
			}
		})

		.done(function(data){
			if(data.error){
				//Do Something
			}
			else {
				console.log("ehlo");
				$("#destination").val(data.output).show();
			}
		});
		event.preventDefault();
	});
});
