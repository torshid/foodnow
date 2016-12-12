$(document).ready(function()
{
    var index = window.location.pathname.indexOf('panel/');

    if (index != -1 && index + 6 < window.location.pathname.length)
    {
        loadPage(window.location.pathname.substr(index + 6));
    }
    else if (window.location.hash.length > 0)
    {
    	loadPage(window.location.hash.substr(1), true);

    	$('#sidebar').scrollTop(0);
    }
    else
	{
        loadPage('overview');
	}

    $(document).on("click", /*"#sidebar a"*/ "a", function(e)
    {
        if ($(this).attr('href') != '#')
        {
            return;
        }
        else
        {
        	loadPage($(this).attr('id'));

            return false;
        }
    })

    $(window).bind('popstate', function(e)
    {
        if (e.originalEvent.state)
        {
        	loadPage(e.originalEvent.state.url, true);
            /*document.getElementById("content").innerHTML = e.originalEvent.state.html;

            if (e.originalEvent.state.title != null)
        	{
            	document.title = e.originalEvent.state.title;
        	}*/
        }
    })

});

function setTitle(title)
{
    document.title = title;
}

function loadPage(url, replace)
{
    var variables = null, realurl = url;

    if (url.indexOf("/") > -1)
    {
        variables = url.substr(url.indexOf("/") + 1).split('/');

        realurl = url.substr(0, url.indexOf("/"));
    }

    $('#content').fadeOut(200,function()
    {
        $('#content').html('<div id="loading"></div>');
        $('#content').fadeIn(200);
    });

    $.ajax(
    {
        type: 'POST',
        url: realurl,
        data: (variables == null ? '' : 'variables[]=' + variables.join('&variables[]=')),
        dataType: "html",
        success: function(msg)
        {
            $('#content').fadeOut(200, function()
            {
                $('#content').fadeIn(200);
                $('#content').html(msg);
                if (replace)
            	{
                	window.history.replaceState({html: msg, title: $(msg).filter('title').text(), url : realurl}, '', realurl);
            	}
                else
            	{
                	window.history.pushState({html: msg, title: $(msg).filter('title').text(), url : realurl}, '', realurl);
                }
        	});

            if ($('#' + realurl).parent().parent().hasClass('navsub'))
            {
                $('#sidebar').find('.active').removeClass('active');

                $('#' + realurl).parent().parent().show();
                $('#' + realurl).parent().parent().parent().first().addClass('active');
            }
            else
            {
                if (!$('#' + realurl).closest('li').hasClass('active')) {
                    $('#sidebar').find('.active').find('.navsub').fadeOut(200);
                }

                $('#sidebar').find('.active').removeClass('active');
            }

            if ($('#' + realurl).parent().parent().hasClass('navsub'))
            {
                $('#' + realurl).addClass('active');
                $('#' + realurl).find('.navsub').fadeIn(200)
            }
            else
            {
                $('#' + realurl).closest('li').addClass('active');
                $('#' + realurl).closest('li').find('.navsub').fadeIn(200);
            }
        },
        error: function()
        {
            $('#content').fadeOut(200,function()
            {
                $('#content').fadeIn(200);
                $('#content').html('Cnt lood pge!!!!11111');
            });
        }
    });
}

function selectside(id)
{
    $('#sidebar').find('.active').removeClass('active');
    $('#' + id).closest('li').addClass('active');
}