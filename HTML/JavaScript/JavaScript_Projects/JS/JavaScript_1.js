function Class_Function() {
    var Class_Output;
    var Classes = document.getElementById("Class_Input").value;
    var Class_String = "You are a ";
    switch(Classes) {
        case "Biohacker":
            Class_Output = Class_String + "Biohacker";
        break;
        case "Envoy":
            Class_Output = Class_String + "Envoy";
        break;
        case "Mechanic":
            Class_Output = Class_String + "Mechanic";
        break;
        case "Mystic":
            Class_Output = Class_String + "Mystic";
        break;
        case "Operative":
            Class_Output = Class_String + "Operative";
        break;
        case "Solarian":
            Class_Output = Class_String + "Solarian";
        break;
        case "Soldier":
            Class_Output = Class_String + "Soldier";
        break;
        case "Technomancer":
            Class_Output = Class_String + "Technomancer";
        break;
        case "Vanguard":
            Class_Output = Class_String + "Vanguard";
        break;
        case "Witchwarper":
            Class_Output = Class_String + "Witchwarper";
        break;
        default:
        Class_Output = "Please enter the class name as written from the above list.";
    }
    document.getElementById("Output").innerHTML = Class_Output;
}

// get element by class name
function Hello_World_Function() {
    var A = document.getElementsByClassName("Click")
    A[0].innerHTML = "The text has changed!";
}

// canvas challenge 216
function token() {
    var c = document.getElementById("token");
    var ctx = c.getContext("2d");
    var img = document.getElementById("murco");
    ctx.drawImage(img,10,10);
}

// gradient
var c = document.getElementById("gradient");
var ctx = c.getContext("2d");

var grd = ctx.createLinearGradient(0, 0, 170, 0);
    grd.addColorStop(0, "black");
    grd.addColorStop(1, "white");

    ctx.fillStyle = grd;
    ctx.fillRect(20, 20, 150, 100);