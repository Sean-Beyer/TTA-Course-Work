function subtraction_function() {
    var Subtraction = 5 - 2;
    document.getElementById("Maths").innerHTML = "5 - 2 =" + Subtraction;
}

function multiplication() {
    var simple_Math= 6*8;
    document.getElementById("Mathm").innerHTML = "6 x 8" + simple_Math;
}

function division() {
    var simple_Math = 48 / 8;
    document.getElementById("Mathd").innerHTML = "48 / 6 =" + simple_Math;
}

function more_Math()  {
    var simple_Math = (1 + 2) * 10 / 2 -5;
    document.getElementById("mMath").innerHTML = "1 plus 2, multiplied by 10, divided in half and then subtracted by 5 equals " + simple_Math;
}

function modulus_Operator() {
    var simple_Math = 25 % 6;
    document.getElementById("dMath").innerHTML = "When you divide 25 by 6 you have remainer of: " + simple_Math;
}

function negation_Operator() {
    var x = 10;
    document.getElementById("MathOp").innerHTML = -x;
}

var X = 5;
X++;
document.write(X)

var Y = 5.25;
Y--;
document.write(Y);

window.alert(Math.random() * 20)

function Floor() {
    document.getElementById("Floor").innerHTML = Math.floor(4.7);
}