function myFunction() {
  var x, text;
  x = document.getElementById("numb").value;
  if (isNaN(x) || x < 1 || x > 10) {
    text = "Aww, you don't want to be friends?";
  } else {
    text = "Who's that calling you?";
  }
  document.getElementById("putin").innerHTML = text;
}