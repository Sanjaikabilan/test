$(document).ready(function () {
    $(window).scroll(function () {
      var scroll = $(window).scrollTop();
      if (scroll > 5) {
        $(".navbar").css("background", "blue");
        console.log("scrolling");
      } else {
        $(".navbar").css("background", "#333");
        console.log("not scrolling");
      }
    });
  });