$(document).ready(function() {

    // Clear default value for the 'name field 'in the Review form
    $('#id_name').val('');
    /*
	    Review form
	*/
    (function($){
        $('#review-form').validate();
    });

    $('#form-group-rating, #review-form input[type="text"], form textarea').on('focus', function() {
        $('#form-group-rating, #form-group-name, #form-group-text').removeClass('has-error');
        if ($(this).find('span.help-block').length){
            $(this).find('span.help-block').remove();
        }
    });
	$('#review-form').submit(function(e) {
		e.preventDefault();
	    $('#form-group-rating, #form-group-name, #form-group-text').removeClass('has-error');
        if ($(this).find('span.help-block').length){
            $(this).find('span.help-block').remove();
        }
	    var postdata = $('#review-form').serialize();
        var span = $(document.createElement('span')).addClass('help-block');
	    $.ajax({
	        type: 'POST',
	        url: $('#review-form').attr('action'),
	        data: postdata,
	        dataType: 'json',
	        success: function(json) {
	            if(json.reviewRating != '') {
	                $('#form-group-rating').addClass('has-error');
                    if ($('#form-group-rating').find('span.help-block').length == 0)
                    {
                        $('#form-group-rating').append(span.html(json.reviewRating));
	                }
                }
	            else if(json.reviewName != '') {
	                $('#form-group-name').addClass('has-error');
                    $('#form-group-name').append(span.html(json.reviewName));
	            }
	            else if(json.reviewText != '') {
	                $('#form-group-text').addClass('has-error');
                    $('#form-group-text').append(span.html(json.reviewText));
	            }
                // No error message has been received from the server
	            if(json.reviewRating == '' && json.reviewName == '' && json.reviewText == '') {
	               $('#review-area').html(
                    '<h3 class="text-center bg-success">Thanks. Your Review has been Posted.</h3>');
	            }
	        }
	    });
	});
});
