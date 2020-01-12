//Array for Bookmarks if already exists in chrome storage it should be reloaded
let bookmarkArray = new Array();
chrome.storage.sync.get(['array'], function (result) {

    if (result.array !== undefined) {
        bookmarkArray = result.array
    }
});

//now the query to get the url of active tab into the input field
let urlfield = document.getElementById("inputUrl");
chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {

    var url = "something went wrong";
    var temp = tabs[0].url.indexOf("#");
    if(temp!=-1){

        url = tabs[0].url.slice(0, temp);
    }else{
    url = tabs[0].url;

    urlfield.value = url;}
});

let titlefield = document.getElementById("inputTitle");
chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
    var title = tabs[0].title;
    titlefield.value = title;

});

//bind butons to variables
let saveBtn = document.getElementById("saveBtn");
let syncBtn = document.getElementById("syncSaves");


//savebutton function (inserting new Bookmarks to array)
saveBtn.addEventListener("click", addToArray);
//syncbutton function (getting a csv out of the array)
syncBtn.addEventListener("click", getCSV);

//for dev purpose only
let removeBtn = document.getElementById("remove");
removeBtn.addEventListener("click", removeData);

function removeData() {
    //removes all data from storage (achtung lokal ist es da bis restart logischerweise)
    chrome.storage.sync.clear();
}

function displayInfo(message) {
    //next function let a message appear for some seconds (together with css)
    document.getElementById("timeoutAlert").innerHTML = '<p>' + message + '</p>';
    document.getElementById("timeoutAlert").style.color = "#333333";

    setTimeout(function () {
        document.getElementById("timeoutAlert").innerHTML = '';
    }, 2000);
}


function addToArray() {
    //function adds inserted Data to an array that can be converted to .csv later
    let tag = "";
    let comment = "";

    let url = document.getElementById("inputUrl").value;
    let title = document.getElementById("inputTitle").value;
    tag = document.getElementById("inputTag").value;
    comment = document.getElementById("inputComment").value;

    bookmarkArray.push([url, title, tag, comment]);

    //chrome storage tauscht das ganze array das persistiert ist gegen das neue aus
    chrome.storage.sync.set({'array': bookmarkArray}, function () {
        //message that it worked, but callback could also be avoided
        //alert("success!");
        console.log("added bookmarkArray to storage")
        displayInfo("...bookmark added")
    });

    document.getElementById("inputTitle").value = " ";
    document.getElementById("inputTag").value = " ";
    document.getElementById("inputComment").value = " ";


    //window.alert("saved Bookmark");
}

function getCSV() {
    //function saves .csv file of the Bookmarks array on local HD for sync with standalone Python

    //alert(bookmarkArray[0]+bookmarkArray[1]+bookmarkArray[2]);
    let csvContent = "data:text/csv;charset=utf-8,";
    bookmarkArray.forEach(function (rowArray) {
        let row = rowArray.join(";");
        csvContent += row + "\r\n";

    });

    //code for downloading the created file
    var encodeUri = encodeURI(csvContent);
    window.open(encodeUri);

    //remove chrome storage, because now we got the file

    removeData();
    displayInfo("...bookmarks synced");
}