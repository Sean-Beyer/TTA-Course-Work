window.alert("It's Murco's Turn");

var A=("Murco said, \"Hooot!!\" as he swooped in for the attack."
+ " a loud \"pop\" is heard as hit shot lands true.");

function rollD20() {
    var d20Result =
    document.getElementById("d20Result");
    var d20 = Math.floor(Math.random()*20+5);
        d20Result.innerHTML = d20;
}