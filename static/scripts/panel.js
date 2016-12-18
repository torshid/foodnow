$(document).ready(function() {
	var index = window.location.pathname.indexOf('panel/');

	if (index != -1 && index + 6 < window.location.pathname.length) {
		loadPage(window.location.pathname.substr(index + 6));
	} else if (window.location.hash.length > 0) {
		loadPage(window.location.hash.substr(1), true);

		$('#sidebar').scrollTop(0);
	} else {
		loadPage('overview', true);
	}

	$(document).on('click', 'a', function(e) {
		if ($(this).attr('href') != '#') {
			return;
		} else {
			if ($(this).children().hasClass('btn-danger')) {
				var ask = confirm("Are you to execute this action?");

				if (!ask) {
					return;
				}
			}

			var form = $(this).closest('form');

			if (form.length) {
				loadPage($(this).attr('id'), true, form.serialize());
			} else {
				loadPage($(this).attr('id'));
			}

			return false;
		}
	})

	$(window).bind('popstate', function(e) {
		if (e.originalEvent.state) {
			loadPage(e.originalEvent.state.url, true);
		}
	})
});

function setTitle(title) {
	document.title = title;
}

function loadPage(url, replace, data, message) {
	var tagid = url;

	var split = window.location.pathname.split('/');
	var root = '/' + split[1] + '/' + split[2] + '/';

	if (url.includes(root)) {
		url = url.replace(root, '');
	}

	var completeurl = root + url;

	if (url.indexOf("/") > -1) {
		tagid = url.substr(0, url.indexOf("/"));
	}

	$('#content').fadeOut(200, function() {
		$('#content').html('<div id="loading"></div>');
		$('#content').fadeIn(200);
	});

	$.ajax({
		type : 'POST',
		url : completeurl,
		data : (data == null ? '' : data),
		dataType : "html",
		success : function(msg) {
			$('#content').fadeOut(200, function() {
				$('#content').fadeIn(200);
				$('#content').html(msg);
				if (message != null) {
					$('#message').html(message);
					$('#message').delay(15000).fadeOut(500);
				}
				if (replace) {
					window.history.replaceState({
						html : msg,
						title : $(msg).filter('title').text(),
						url : completeurl
					}, '', completeurl);
				} else {
					window.history.pushState({
						html : msg,
						title : $(msg).filter('title').text(),
						url : completeurl
					}, '', completeurl);
				}
			});

			if ($('#' + tagid).parent().parent().hasClass('navsub')) {
				$('#sidebar').find('.active').removeClass('active');

				$('#' + tagid).parent().parent().show();
				$('#' + tagid).parent().parent().parent().first().addClass(
						'active');
			} else {
				if (!$('#' + tagid).closest('li').hasClass('active')) {
					$('#sidebar').find('.active').find('.navsub').fadeOut(200);
				}

				$('#sidebar').find('.active').removeClass('active');
			}

			if ($('#' + tagid).parent().parent().hasClass('navsub')) {
				$('#' + tagid).addClass('active');
				$('#' + tagid).find('.navsub').fadeIn(200)
			} else {
				$('#' + tagid).closest('li').addClass('active');
				$('#' + tagid).closest('li').find('.navsub').fadeIn(200);
			}
		},
		error : function() {
			$('#content').fadeOut(200, function() {
				$('#content').fadeIn(200);
				$('#content').html('Cnt lood pge!!!!11111');
			});
		}
	});
}