$(document).ready(function() {
    /*
	    Review form
	*/
    (function($){
        $('#review-form').validate();
    });

    $('#review-form input[type="text"], form textarea').on('focus', function() {
        $('form input[type="text"], form textarea').removeClass('has-error');
    });
	$('form').submit(function(e) {
		e.preventDefault();
	    $('form #id-rating, form #id_name, form #id_text').removeClass('has-error');
	    var postdata = $('form').serialize();
	    $.ajax({
	        type: 'POST',
	        url: '/products/review/',
	        data: postdata,
	        dataType: 'json',
	        success: function(json) {
	            if(json.reviewRating != '') {
	                $('form #id-rating').addClass('has-error');
	            }
	            if(json.reviewName != '') {
	                $('form #id_name').addClass('has-error');
	            }
	            if(json.reviewText != '') {
	                $('form #id_text').addClass('has-error');
	            }
                // No error message has been received from the server
	            if(json.emailMessage == '' && json.subjectMessage == '' && json.messageMessage == '') {
	                $('#review-form').fadeOut('fast', function() {
	                    $('.#review-form').append('<p class="flow-text center-align">Thanks. Your Review has been Posted.</p>');
	                });
	            }
	        }
	    });
	});
});
