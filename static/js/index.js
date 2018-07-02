




$(function () {


    $('.carousel').carousel()
//marketing particular display, hover show start -----------------------
    $(".marketing .col-lg-4 p a").hover(function () {
        $(this).parent().next().stop().toggle(800)
    } )
//marketing particular display, hover show stop -----------------------

//marketing images animate start---------------------------------------
    $(".marketing .col-lg-4 img").hover(function () {
        $(this).stop().animate({"width":"170px","height":"170px"},200)
    },function () {
        $(this).stop().animate({"width":"140px","height":"140px"},200)
    })
//marketing images animate stop---------------------------------------

})