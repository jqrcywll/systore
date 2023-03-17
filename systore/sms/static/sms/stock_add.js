function addOneLine() {
    var element = document.getElementsByTagName("table")[0];
    var newLine = document.getElementById("template").cloneNode(true);
    newLine.removeAttribute("id");
    newLine.removeAttribute("style");
    element.appendChild(newLine);
    return newLine;
}

function addStockEvent() {
    count = 0;
    var no = 0;
    var barcode = "";
    var lastInputTime = new Date().getTime();
    document.body.onkeydown = function (e) {
        var curInputTime = new Date().getTime();
        if (barcode.length == 0) {
            barcode = e.key;
        } else {
            if (curInputTime - lastInputTime < 300) {
                barcode += e.key;
                if (barcode.length >= 13) {
                    var newLine = addOneLine();
                    newLine.children[0].innerText = (++no).toString();
                    newLine.children[1].firstChild.setAttribute("value", barcode);
                    newLine.children[2].firstChild.setAttribute("value", "晨光自动笔3mm");
                    newLine.children[4].firstChild.setAttribute("value", "晨光");
                    barcode = "";

                    document.getElementById("count").innerHTML = ++count;
                }
            } else {
                barcode = e.key;
            }
        }
        lastInputTime = curInputTime;
    };
}

function fillWord(that) {
    var word = that.innerText;
    var allFillPositions = document.getElementsByClassName("fill_word_position");
    var pos;
    for (pos = 0; pos < allFillPositions.length; pos++) {
        if (allFillPositions[pos].checked) {
            allFillPositions[pos].nextSibling.setAttribute("value", word);
            allFillPositions[pos].checked = false;
        }
    }
}

function removeThisLine(that) {
    that.parentNode.parentNode.remove();
    document.getElementById("count").innerHTML = --count;
}

window.onload = addStockEvent;