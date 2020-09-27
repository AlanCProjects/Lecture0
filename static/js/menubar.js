if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
    console.debug("Movile version")
   }

$(document).ready(function(){
    
        $('#login').click(function(e) {
            //when the user do click on "login"
            $('#login-container').toggleClass('menu-right')
            $('#login-container').toggleClass('active-menu-right')
            
        });
}); 