var X = 10;
function Add_numbers_1() {
    console.log(15 + X)
}
function Add_numbers_2() {
    console.log(X + 100);
}
Add_numbers_1();
Add_numbers_2();

// two

function addZero(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i
}

function get_Date() {
    var d = new Date();
    var x = document.getElementById("Greeting");
    var h = addZero(d.getHours());
    var m = addZero(d.getMinutes());
    var s = addZero(d.getSeconds());
    x.innerHTML = h + ":" + m + ":" + s;
}

// three

function whattime() {
    var time= new Date().getHours();
    if (time > 22) {
        document.getElementById("bedtime").innerHTML = "Get to bed, you nerd!!!";
    }
}

// four

function diceroll() {
    var baddyac = 11
    var dice = Math.floor(Math.random() * 20);
    if (bonus + dice > baddyac) {
        document.getElementById("resolve").innerHTML = "And you kill the terrible beastie!!";
    }
    else {
        document.getElementById("resolve").innerHTML = "Your shot goes wide...";
    }
}

//five

function Time_function() {
    var Time = new Date().getHours();
    var Reply;
    if (Time < 12 == Time > 0) {
        Reply = "It is morning time!";
    }
    else if (Time > 12 == Time < 18) {
        Reply = "It is the afternoon.";
    }
    else {
        Reply = "It is evening time.";
    }
    document.getElementById("Time_of_day").innerHTML = Reply;
}