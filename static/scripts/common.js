$(document).ready(function() {
	$(".restolike_btn").click(function () {
		alert($(this).data("id"));
	    $(this).text("Liked");
	    $(this).removeClass("btn-primary").addClass("btn-default");

	});

	$(".dishlike_btn").click(function () {
		alert($(this).data("id"));
	    $(this).text("Liked");
	    $(this).removeClass("btn-primary").addClass("btn-default");
	});
});