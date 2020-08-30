function Ride_Function() {
    var Height, Can_ride;
    Height = document.getElementById("Height") .value;
    Can_ride = (Height < 52) ? "You are too short":"You are tall enough";
    document.getElementById("Ride").innerHTML = Can_ride + " to ride.";
}

function SF(Race, Theme, Class, Special) {
    this.SF_Race = Race;
    this.SF_Theme = Theme;
    this.SF_Class = Class;
    this.SF_Special = Special;
}
var kAPP = new SF("Android", "Tinkerer", "Mechanic", "Drone");
var Dennea = new SF("Lashunta", "Ace Pilot", "Solarian", "Solar Armor");
var abstract = new SF("Tiefling", "Icon", "Soldier/Envoy", "Clever Feint");
function myFunction() {
    document.getElementById("New_and_This").innerHTML = "kAPP is a " + kAPP.SF_Race + kAPP.SF_Class + " who travels the galaxy with Murco, his " + kAPP.SF_Special;
}

function myFunk() {
    document.getElementById("New_and_This").innerHTML = "Ray is an abstract " + abstract.SF_Race + abstract.SF_Class + " who specializes in the " + abstract.SF_Special;
}

function count_Function() {
    document.getElementById("Counting").innerHTML = Count();
    function Count() {
        var Starting_Point = 9;
        function Plus_one() {Starting_Point += 1;}
        Plus_one();
        return Starting_Point;
    }
}