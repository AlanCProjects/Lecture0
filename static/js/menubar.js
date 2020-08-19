$(document).ready(function(){
    var LoginClick = 0; //click checker 0 = false, 1 = true
    console.log(LoginClick)
        $('#login').click(function(e) {
         //when the user do click on "login"
        $('#login-container').toggleClass('menu-right')
        $('#login-container').toggleClass('active-menu-right')
            
        });
}); 