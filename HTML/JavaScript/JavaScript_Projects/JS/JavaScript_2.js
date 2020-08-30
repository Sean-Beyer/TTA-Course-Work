function validateForm() {
    var x = document.forms["myform"]["fname"].value;
    if (x == "") {
        alert("Please enter your name");
        return false;
    }
}