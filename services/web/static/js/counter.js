$( document ).ready(function() {
	$( '#incrButton' ).on( 'click', incrButtonClicked );
})

function incrButtonClicked() {
	console.log('click');
	$.ajax({
  		url: '/counter',
		success: setCounter
  	});
}

function setCounter(value) {
	$( '#counter' ).text(value)
}
