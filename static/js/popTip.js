// µØ≥ˆÃ· æ
popTip = function (msg,time) {
    $(".pop-tip p").text(msg);
    // var popTipW = $(".pop-tip p").width();
    // alert(popTipW)
    // var windowW = $(window).width();
    // $(".pop-tip p").css({"left":(windowW - popTipW)/2 + "px"});
    $(".pop-tip").show();
    //setTimeout(function () {
    //    $(".pop-tip").hide();
    //}, time)
}
