$(document).ready(function () {
    $(window).scroll(function () {
      var scroll = $(window).scrollTop();
      if (scroll > 5) {
        $(".black").css("background", "blue");
      } else {
        $(".black").css("background", "#333");
      }
    });
  });