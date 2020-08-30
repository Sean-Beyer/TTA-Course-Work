document.write(typeof 3);

function my_Function() {
    document.getElementById("Test").innerHTML = 0/0;
}

function my_Function1() {
    document.getElementById("Test1").innerHTML = isNaN('This is a string');
}

function my_Function2() {
    document.getElementById("Test2").innerHTML = isNaN('007');
}

document.write(2E310);

document.write(-2E310);

document.write(10 > 2);

document.write(10 < 2);

console.log(2 + 2)

document.write("10" + 5);

console.log(15 > 25)

document.write(10 == 10)

document.write(10 == 5)

X = 10;
Y = 10;
document.write(X === Y);

A = 82;
B = "82";
document.write(A === B);

C = "Ten";
D = 10;
document.write(C === D)

E = "Data";
F = 10;
document.write(E === F)

document.write(5 > 2 && 10 > 4);

document.write(5 < 2 && 10 > 4);

document.write(5 > 10 || 10 > 4);

document.write(5 < 10 || 10 > 4);

function not_Function() {
    document.getElementById("Not").innerHTML = !(5 > 10);
}

function not_Function2() {
    document.getElementById("Not2").innerHTML = !(20 > 10);
}