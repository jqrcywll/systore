function addOneLine() {
    var newLine;
    const tbody = document.getElementsByTagName("tbody")[0];
    var tpl = document.getElementById("tpl");
    if (!tpl) {
        newLine = tbody.lastElementChild.cloneNode(true);
    } else {
        newLine = tpl.cloneNode(true);
        tpl.remove();
    }
    newLine.removeAttribute("id");
    newLine.removeAttribute("style");
    tbody.appendChild(newLine);
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
                    newLine.children[2].firstChild.setAttribute("value", "晨光自动笔");
                    newLine.children[3].firstChild.setAttribute("src", "https://res-showapi.oss-cn-hangzhou.aliyuncs.com/barcode/20220114/70e06a59-9b47-4e88-b2a3-348c7c940f11.jpg");
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

function removeThisLine(that) {
    that.parentNode.parentNode.remove();
    document.getElementById("count").innerHTML = --count;
}

window.onload = addStockEvent;