$( document ).ready(function() {
	$( '#loginButton' ).on( 'click', loginButtonClicked );
})

function loginButtonClicked() {
	var name = $( '#username' ).val();
	var pwd = $( '#password' ).val();
	var jsonData = JSON.stringify({'name': name, 'pwd': pwd});

	$.ajax({
  		url: `${app_host}/login`,
			type: "POST",
    	dataType: "json",
    	data: jsonData,
    	contentType: "application/json",
			success: succesfullyLoggedIn,
			error: loginError
  	});
}



function loginError(XMLHttpRequest, textStatus, errorThrown) {
	console.log('error logging in');
	$( '#error' ).text(textStatus);
}

function succesfullyLoggedIn(response) {
	//var obj = JSON.parse(response)
	token = response['token']
	userId = response['id']
	window.sessionStorage.setItem('token', token)
	console.log('successfully logged in');
	$( '#error' ).text("");
	url = `/user?access_token=${token}`;
	window.location.href = url
}
