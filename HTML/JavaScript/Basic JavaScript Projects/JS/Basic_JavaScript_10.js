// Loop
function count_To_Ten() {
    var Digit = "";
    var X = 1;
    while (X < 11) {
        Digit += "<br>" + X;
        X++;
    }
    document.getElementById("Counting_to_Ten").innerHTML = Digit;
}

// String Length
function myFunction() {
    var str = "Hello World!";
    var n = str.length;
    document.getElementById("demo").innerHTML = n;
}

// for loop
var Instruments = ["Guitar", "Drums", "Piano", "Bass", "Violin", "Trumpet", "Flute"];
var Content = "";
var Y;
function for_Loop() {
    for (Y = 0; Y < Instruments.length; Y++){
    Content += Instruments[Y] + "<br>";
    }
    document.getElementById("List_of_Instruments").innerHTML = Content;
}

// Array
function kapp_pics() {
    var kAPP_Pictures = [];
    kAPP_Pictures[0] = "V1";
    kAPP_Pictures[1] = "V2";
    kAPP_Pictures[2] = "MV1";
    kAPP_Pictures[3] = "MV2";
    document.getElementById("kapp").innerHTML = "This is kAPP at Level 1 " + kAPP_Pictures[0] + ".";
}

// constant
function constant_function() {
    const Musical_Instrament = {type:"guitar", brand:"Fender", color:"black"};
    Musical_Instrament.color = "blue";
    Musical_Instrament.price = "$900";
    Musical_Instrament.strings = "Thick";
    document.getElementById("Constant").innerHTML = "The cost of the " + Musical_Instrament.color + Musical_Instrament.type + " was " + Musical_Instrament.price;
    document.getElementById("Constant").innerHTML = "This one was also made by " + Musical_Instrament.brand;
}

// Let
function funkything() {
    {
        let x = 3;
        document.getElementById("thingy").innerHTML = x;
    }
    {
        let x = 4;
        document.getElementById("thingy2").innerHTML = x;
    }
}

// return
function myFunction(name) {
    return "Hello " + name;
}
document.getElementById("action").innerHTML = myFunction("Sean");