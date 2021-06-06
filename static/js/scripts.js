$( document ).ready(function(){
	function asyncMovePage(url){
		let url = new URL(window.location.href)
	
		let ajaxOption = {
			url : url,
			async : true,
			type : "GET",
			dataType : "html"
		};

		$.ajax(ajaxOption).done(function(data){
			$("#card-wrapper").load(url);
			// Contents 영역 삭제
			$('#card-wrapper').children().remove();
			// Contents 영역 교체
			$('#card-wrapper').html(data);
		});
	}
});
$(".bookcard").click(function () {
  let id = $(this).closest("div").attr("id");
  idTag = $("#" + id);
  textParts = idTag.children(".card-body")
  // console.log(textParts)
  if (textParts.css("display") == "block") {
    textParts.hide();
  } else {
    textParts.show();
  }
});

// $( document ).ready(function() {
// 	$("#books").click(function() {
// 		$("#card-wrapper").load('/book/library/');
// 		return false;
// 	});
// });



// // sign up
// $( "form[ name = signupForm ]" ).submit(function(e) {

// 	let $form = $(this);
// 	let $error = $form.find(".error");
// 	let data = $form.serialize();

// 	$.ajax({
// 		url: "/user/signup",
// 		type: "POST",
// 		data: data,
// 		dataType: "json",
// 		success: function(response) {
// 			window.location.href="/dashboard/";
// 		},
// 		error: function(response) {
// 			console.log(response);
// 			$error.text(response.responseJSON.error).removeClass("error-hidden");
// 		}
// 	})

// 	e.preventDefault();

// });


// var xhttp = new XMLHttpRequest();
//   xhttp.open("GET", "test.jsp");
//   xhttp.onreadystatechange = function() {
//     if (xhttp.readyState == 4 && xhttp.status == 200) {
//       document.getElementById("Context").innerHTML = xhttp.responseText;
//     }
//   };
//   xhttp.send();




// $( document ).ready(function(){
// 	function asyncMovePage(url){
	
// 		let ajaxOption = {
// 			url : url,
// 			async : true,
// 			type : "GET",
// 			dataType : "html"
// 		};

// 		$.ajax(ajaxOption).done(function(data){
// 			$("#card-wrapper").load(url);
// 			// Contents 영역 삭제
// 			$('#card-wrapper').children().remove();
// 			// Contents 영역 교체
// 			$('#card-wrapper').html(data);
// 		});
// 	}
// });

		// document.querySelector('#card-wrapper')

		// window.location.href


		// $("#card-wrapper").load('/')

// window.onload = function(){
// 	const navContainer = document.querySelector(".tab-menu");
// 	const navItems = navContainer.children;

// 	for (let i = 0; i < navItems.length; i++) {
// 		navItems[i].addEventListener("click", function() {
// 		let current = document.getElementsByClassName("active");
// 		if (current.length > 0) { 
// 			current[0].className = current[0].className.replace(" active", "");
// 		}
// 		this.className += " active";
// 		});
// 	}


