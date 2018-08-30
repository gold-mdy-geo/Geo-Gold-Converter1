$(document).ready(function() {
	$('label[for=source]').change(function() {
		if(this.value == 'Zawgyi') {
			$('#source').css("font-family", "Zawgyi-One")
			console.log("Source is Zawgyi-One");
		}
		if(this.value == 'Unicode') {
			$('#source').css("font-family", "Pyidaungsu");
		}
		if(this.value == 'WinMyanmar'){
			$('#source').css("font-family", "win_innwaregular");
		}
	});

	$('label[for=source]').change(function(){
		if(this.value == 'Zawgyi') {
			$("#destination").css("font-family", "Zawgyi-One")
			console.log("Desination is Zawgyi-One");
		}
		if (this.value == 'Unicode') {
			$("#destination").css("font-family", "Pyidaungsu");
		}
		if (this.value == 'WinMyanmar'){
			$("#destination").css("font-family", "win_innwaregular");		
		}
	});
});
