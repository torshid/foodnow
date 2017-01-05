function perform(change, plate, category) {
	var totalCategoryPrice = parseInt(document.getElementById('ordcatprice'
			+ category).innerHTML);

	var platePrice = parseInt(document.getElementById('menplaprice' + plate).innerHTML);

	var plateRepetition = parseInt(document.getElementById('menplacount'
			+ plate).innerHTML);

	plateRepetition += change;

	if (plateRepetition < 0) {
		plateRepetition = 0;

		document.getElementById('ordplaline' + plate).style.display = 'none';
	} else {
		totalCategoryPrice += change * platePrice;

		document.getElementById('subtotal').innerHTML = parseInt(document
				.getElementById('subtotal').innerHTML)
				+ change * platePrice;

		if (plateRepetition <= 0) {
			document.getElementById('ordplaline' + plate).style.display = 'none';
		} else {
			document.getElementById('ordplaline' + plate).style.display = 'table-row';
		}
	}

	if (totalCategoryPrice < 0) {
		totalCategoryPrice = 0;
	}

	document.getElementById('ordcatprice' + category).innerHTML = totalCategoryPrice;

	document.getElementById('menplacount' + plate).innerHTML = plateRepetition;

	document.getElementById('ordplacount' + plate).innerHTML = plateRepetition;
}

var detail = 0;

function order() {
	alert('hello');
}

$(document).on(
		"click",
		".open-modalPictureView",
		function() {
			var itemId = $(this).data('id');
			$(".modal-header #modalPictureName")
					.html($("#ite" + itemId).html());
			$(".modal-body #modalPictureImage").attr(
					'src',
					'<?php echo $this->getOrigin() . PATH_PLATES ?>' + itemId
							+ '.jpg');
		});

function scrollTo(id) {
	$('html,body').animate({
		scrollTop : $("#" + id).offset().top
	}, 'slow');
}

$(document)
		.ready(
				function() {
					$("#orderSubmit")
							.click(
									function() {
										$('#submitError').html('');

										if ($('#subtotal').html() == '0') {
											$('#submitError')
													.html(
															'<div class="alert alert-danger" style="margin-bottom: 20px;"><span type="button" class="close" data-dismiss="alert">&times;</span>You have to select some plates.</div>');

											scrollTo('submitError');

											return false;
										}

										$('html, body').animate({
											scrollTop : 0
										}, 'fast');
									});
				});

function setCookie(name, value, days) {
	var exdate = new Date();

	exdate.setDate(exdate.getDate() + days);

	value = escape(value)
			+ ((days == null) ? '' : '; expires=' + exdate.toUTCString());

	document.cookie = name + '=' + value;
}

function getCookie(name) {
	var value = document.cookie;

	var start = value.indexOf(' ' + name + '=');

	if (start == -1) {
		start = value.indexOf(name + "=");
	}
	if (start == -1) {
		value = null;
	} else {
		start = value.indexOf('=', start) + 1;

		var end = value.indexOf(';', start);

		if (end == -1) {
			end = value.length;
		}

		value = unescape(value.substring(start, end));
	}

	return value;
}