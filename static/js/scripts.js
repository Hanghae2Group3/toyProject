// sign up
$( "form[ name = signupForm ]" ).submit(function(e) {

	let $form = $(this);
	let $error = $form.find(".error");
	let data = $form.serialize();

	$.ajax({
		url: "/user/signup",
		type: "POST",
		data: data,
		dataType: "json",
		success: function(response) {
			window.location.href="/dashboard/";
		},
		error: function(response) {
			console.log(response);
			$error.text(response.responseJSON.error).removeClass("error-hidden");
		}
	})

	e.preventDefault();

});


// log in
$( "form[ name = loginForm ]" ).submit(function(e) {

	let $form = $(this);
	let $error = $form.find(".error");
	let data = $form.serialize();

	$.ajax({
		url: "/user/login",
		type: "POST",
		data: data,
		dataType: "json",
		success: function(response) {
			window.location.href="/dashboard/";
		},
		error: function(response) {
			console.log(response);
			$error.text(response.responseJSON.error).removeClass("error-hidden");
		}
	})

	e.preventDefault();

});