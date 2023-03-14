function addOneLine() {
    const element = document.getElementsByTagName("table")[0];
    const newLine = document.getElementById("template").cloneNode(true);
    newLine.removeAttribute("id");
    newLine.removeAttribute("style");
    element.appendChild(newLine);
}
