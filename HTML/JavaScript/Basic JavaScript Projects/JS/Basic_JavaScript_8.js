// concat

function full_sentance() {
    var part_1 = "I have ";
    var part_2 = "made this ";
    var part_3 = "into a complete ";
    var part_4 = "sentance.";
    var whole_sentence = part_1.concat(part_2, part_3, part_4);
    document.getElementById("statement").innerHTML = whole_sentence;
}

// slice

function slice_method() {
    var sentence = "All work and now play makes Johnny a dull boy.";
    var section = sentence.slice(27,33);
    document.getElementById("slice").innerHTML = section;
}

// uppercase

function uppercase() {
    var str = "This will be uppercase!";
    var res = str.toUpperCase();
    document.getElementById("up").innerHTML = res;
}

// search

function search() {
    var str = "I am making a string";
    var thing = str.search("string");
    document.getElementById("thingy").innerHTML = thing;
}

// number method

function string() {
    var x = 182;
    document.getElementById("nums_to_string").innerHTML = x.toString();
}

// precision method

function precision_Method() {
    var X = 12938.3012987376112;
    document.getElementById("doit").innerHTML = X.toPrecision(10);
}

// fix

function myFunction() {
    var num = 5.56789;
    var n = num.toFixed(2);
    document.getElementById("display").innerHTML = n;
}