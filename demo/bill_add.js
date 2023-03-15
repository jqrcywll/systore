function addOneLine() {
    var element = document.getElementsByTagName("table")[0];
    var newLine = document.getElementById("template").cloneNode(true);
    newLine.removeAttribute("id");
    newLine.removeAttribute("style");
    element.appendChild(newLine);
}