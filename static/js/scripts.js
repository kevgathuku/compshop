$(document).ready(function() {

    // Clear default value for the 'name field 'in the Review form
    $('#id_name').val('');
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
	            if(json.reviewRating == '' && json.reviewName == '' && json.reviewText == '') {
	               $('#review-area').replaceWith(
                    '<h3 class="text-center bg-success">Thanks. Your Review has been Posted.</h3>');
	            }
	        }
	    });
	});
});
