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

function setCounter(result) {
	var obj = JSON.parse(result)
	$( '#counter' ).text(obj['value'])
}
