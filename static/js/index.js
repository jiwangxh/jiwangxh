




$(function () {


    $('.carousel').carousel()
//marketing particular display, hover show start -----------------------
    $(".marketing .col-lg-4 p a").hover(function () {
        $(this).parent().next().toggle(800)
    },function () {
        $(this).parent().next().toggle(800)
    })
//marketing particular display, hover show stop -----------------------

//marketing images animate start---------------------------------------
    $(".marketing .col-lg-4 img").hover(function () {
        $(this).animate({"width":"+=20px","height":"+=20px"},400)
    },function () {
        $(this).animate({"width":"-=20px","height":"-=20px"},400)
    })
//marketing images animate stop---------------------------------------

})