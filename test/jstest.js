function asyncMovePage(url){
	// ajax option
	var ajaxOption = {
		url : url,
		async : true,
		type : "POST",
		dataType : "html",
		cache : false
	};

	$.ajax(ajaxOption).done(function(data){
		//  
		$('#card-wrapper').children().remove();
		// 
		$('#card-wrapper').html(data);
	});
}



window.onload = function() { 
	let path = window.location.pathname;

	let navContainer = document.getElementByClassName("tab-menu")
	let navItem = navContainer[0].children

	for (let i = 0; i < navItem.length; i++) {
		navItem[i].addEventListener("click", function() {
			let current = document.getElementsByClassName("active");
			if (current.length > 0) { 
				current[0].className = current[0].className.replace(" active", "");
			}
			this.className += " active";
			});
	}	

window.onload = function() { 
	let path = window.location.pathname;
	
	switch (path) {
		case "/user/signup/":
			document.getElementById("signup").classList.add("active");
			break;

		case "/user/login/":
			document.getElementById("login").classList.add("active");
			break;	

		case "/user/dashboard/":
			document.getElementById("dashboard").classList.add("active");
			break;

		case "/book/cart/":
			document.getElementById("cart").classList.add("active");
			break;

		case "/book/library/":
			document.getElementById("library").classList.add("active");
			break;
