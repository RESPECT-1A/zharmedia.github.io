$(document).ready(function () {

	// Smooth scroll
	$("a[target=self]").on('click', function(event) {
		$('html, body').animate({scrollTop: $(this.hash).offset().top - 100},'slow');
		return false;
	});

	  // Get Viewport
	  var width = $(window).width();
	  if (width < 575) {
		  $('div').removeAttr('data-wow-delay');
	  }
});

// Fixed menu when scrolling
$(window).scroll(function (event) {
	var scroll = $(window).scrollTop();
	if(scroll > 0){
		$('nav').addClass('navbar-white');
	} else{
		$('nav').removeClass('navbar-white');
	}
});

// Tooltip
$('[data-toggle="tooltip"]').tooltip();

// Wow JS
new WOW().init();
