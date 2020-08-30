// Break
var text = "";
var i;
for (i = 0; i < 10; i++) {
    if (i === 3) { break; }
    text += "The number is " + i + "<br>";
}
document.getElementById("break").innerHTML = text;

// Continue
var stuff = "";
var j;
for (j = 0; j < 10; j++) {
    if (j === 3) { continue; }
    stuff += "The number is " + j + "<br>";
}
document.getElementById("continue").innerHTML = stuff;