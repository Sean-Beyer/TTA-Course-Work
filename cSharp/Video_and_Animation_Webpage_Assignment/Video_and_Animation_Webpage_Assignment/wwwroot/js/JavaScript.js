    var width = $(window).width();
    var height = $(window).height();
    var upleft = 0;
 function goRight() {
        $("#animate").animate({
        left: width
      }, 5000, function() {
         setTimeout(goLeft, 50);
      });
    }
    function goLeft() {
        $("#animate").animate({
        left: 0
      }, 5000, function() {
         setTimeout(goRight, 50);
      });
    }
    function goUp() {
        $("#animate").animate({
        top: 0
      }, 5000, function() {
         setTimeout(goDown, 50);
      });
    }
    function goDown() {
        $("#animate").animate({
        top: height
      }, 5000, function() {
         setTimeout(goUp, 50);
      });
    }
    setTimeout(goRight, 50);

$("#animate").on('click',function(){$('#animate').stop();
    if(upleft == 0)
    {goDown(); upleft=1;}
    else {goLeft();upleft=0}
})