
jQuery(document).ready(function() {

    $('.page-container .submit').click(function(){
        var boy = $(this).find('.boy').val();
        var girl = $(this).find('.girl').val();
        var mettingtime = $(this).find('.mettingtime').val();

        if(boy == '') {
            $(this).find('.error').fadeOut('fast', function(){
                $(this).css('top', '27px');
            });
            $(this).find('.error').fadeIn('fast', function(){
                $(this).parent().find('.boy').focus();
            });
            return false;
        }
        if(girl == '') {
            $(this).find('.error').fadeOut('fast', function(){
                $(this).css('top', '96px');
            });
            $(this).find('.error').fadeIn('fast', function(){
                $(this).parent().find('.girl').focus();
            });
            return false;
        }
        if(mettingtime == '') {
            $(this).find('.error').fadeOut('fast', function(){
                $(this).css('top', '96px');
            });
            $(this).find('.error').fadeIn('fast', function(){
                $(this).parent().find('.mettingtime').focus();
            });
            return false;
        }
    });

    $('.page-container form .username, .page-container form .password').keyup(function(){
        $(this).parent().find('.error').fadeOut('fast');
    });

});
