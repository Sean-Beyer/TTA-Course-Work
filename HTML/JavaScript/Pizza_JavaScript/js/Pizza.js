function getReceipt() {
    // This initializes out string so it can get passesed from
    // function to function, growing line by line into a full reciept
    var text1 = "<h3>You Ordered:</h3>";
    var runningTotal = 0;
    var sizeTotal = 0;
    var sizeArray = document.getElementsByClassName("size");
    for (var i = 0; i < sizeArray.length; i++) {
        if (sizeArray[i].checked) {
            var selectedSize = sizeArray[i].value;
            text1 = text1+selectedSize+"<br>";
        }
    }
    if (selectedSize === "Personal Pizza") {
        sizeTotal = 6;
    } else if (selectedSize === "Small Pizza") {
        sizeTotal = 8;
    } else if (selectedSize === "Medium Pizza") {
        sizeTotal = 10;
    } else if (selectedSize === "Large Pizza") {
        sizeTotal = 14;
    } else if (selectedSize === "Extra Large Pizza") {
        sizeTotal = 16;
    }
    runningTotal = sizeTotal;
    console.log(selectedSize+" = $"+sizeTotal+".00");
    console.log("size text1: "+text1);
    console.log("subtotal: $"+runningTotal+".00");
    // these variables will be passed on to each function
    getMeat(runningTotal,text1);
};
function getVegetable(runningTotal,text1) {
    var veggieTotal = 0;
    var selectedVegetable = [];
    var veggieArray = document.getElementsByClassName("veggies");
    for (var j = 0; j < veggieArray.length; j++) {
        if (veggieArray[j].checked) {
            selectedVegetable.push(veggieArray[j].value);
            console.log("selected veggie item: ("+veggieArray[j].value+")");
            text1 = text1+veggieArray[j].value+"<br>";
        }
    }
    var veggieCount = selectedVegetable.length;
    if (veggieCount > 1) {
        veggieTotal = (veggieCount - 1);
    } else {
        veggieTotal = 0;
    }
    runningTotal = (runningTotal + veggieTotal);
    console.log("total selected veggie items: "+veggieTotal);
    console.log(veggieCount+" veggie - 1 free veggie = "+"$"+veggieTotal+".00");
    console.log("veggie text1: "+text1);
    console.log("Purchase Total: "+"$"+runningTotal+".00");
    document.getElementById("showText").innerHTML=text1;
    document.getElementById("totalPrice").innerHTML = "<h3>Total: <strong>$"+runningTotal+".00"+"</strong></h3>";
}
function getMeat(runningTotal,text1) {
    var meatTotal = 0;
    var selectedMeat = [];
    var meatArray = document.getElementsByClassName("meats");
    for (var j = 0; j < meatArray.length; j++) {
        if (meatArray[j].checked) {
            selectedMeat.push(meatArray[j].value);
            console.log("selected meat item: ("+meatArray[j].value+")");
            text1 = text1+meatArray[j].value+"<br>";
        }
    }
    var meatCount = selectedMeat.length;
    if (meatCount > 1) {
        meatTotal = (meatCount - 1);
    } else {
        meatTotal = 0;
    }
    runningTotal = (runningTotal + meatTotal);
    console.log("total selected meat items: "+meatTotal);
    console.log(meatCount+" meat - 1 free meat = "+"$"+meatTotal+".00");
    console.log("meat text1: "+text1);
    console.log("Purchase Total: "+"$"+runningTotal+".00");
    document.getElementById("showText").innerHTML=text1;
    document.getElementById("totalPrice").innerHTML = "<h3>Total: <strong>$"+runningTotal+".00"+"</strong></h3>";
}