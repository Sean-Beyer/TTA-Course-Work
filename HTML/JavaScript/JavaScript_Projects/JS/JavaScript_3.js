function displayType(feature) {
    var featureType = feature.getAttribute("data-feature-type");
    alert(feature.innerHTML + " is a feature of the " + featureType + ".")
}