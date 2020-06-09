$(document).ready(function(){
    var LoginClick = 0; //click checker 0 = false, 1 = true
    console.log(LoginClick)
    if ( LoginClick == 0){
        $('#login').click(function(e) {
            //when the user do click on "login"
            e.stopPropagation();
            if (LoginClick == 0){
                //if checker is false (0) add class active-menu-right (in CSS show the options)
                $('#login-container').addClass('active-menu-right')
                LoginClick = 1;
            } else {
                //If not remove class active-menu-right (in CSS)
                $('#login-container').removeClass('active-menu-right')
                LoginClick = 0;
            }
        });
    }
        $(window).click(function() {
            // If user clock outside of "active-menu-right" remove the class "active-menu-right"
            if (LoginClick == 1){
                $('#login-container').removeClass('active-menu-right')
                LoginClick = 0;
            }
        });
}); 