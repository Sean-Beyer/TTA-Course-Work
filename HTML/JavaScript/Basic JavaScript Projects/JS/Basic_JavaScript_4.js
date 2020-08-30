function my_Dictionary() {
    var kAPP = {
        Race:"Android",
        Theme:"Tinkerer",
        Class:"Mechanic",
        Level:1,
        AI:"Drone",
    };
    delete kAPP.Class
    document.getElementById("Dictionary").innerHTML = kAPP.Class
}