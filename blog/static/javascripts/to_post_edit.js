function add_images(name) {
    var option = window.opener.document.getElementById('id_text')
    var nowArray = option.value.split("\n");
    var imageset = "";
    if (nowArray.length == 0) {
        imageset = "<img src=" + name + " /> <br>";
    } else {
        imageset = "<br><img src=" + name + " /><br>";
    }

    nowArray.push(imageset)
    var resArray = [];
    for (var i = 0; i < nowArray.length; i++) {
        if (nowArray[i].length > 0) {
            resArray.push(nowArray[i]);
        }
    }

    var retString = "";
    for (var i = 0; i < resArray.length; i++) {
        retString += resArray[i] + "\n";
    }
    option.value = retString;
}

function PopupOpener(name) {
    window.open(name, 'subwin', 'width=500,height=500')
}